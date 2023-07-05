import { Types } from 'mongoose';
import { NextFunction, Request, Response } from 'express';

import catchAsync from '../utils/catchAsync';
import AppError from '../utils/AppError';
import { QueryString } from '../utils/ApiFeatures';

interface Services {
  createOne: (data: {}, objectId: Types.ObjectId) => Promise<object | null>;
  getAll: (query: QueryString) => Promise<object[]>;
}

export const createOne = <T extends Services>(ModelService: T) =>
  catchAsync(async (req: Request, res: Response, next: NextFunction) => {
    const userId = req.user?._id;
    if (!userId) {
      return next(new AppError('Please Login!', 401));
    }

    const objectId = new Types.ObjectId(userId);

    const data = await ModelService.createOne(req.body, objectId);

    res.status(201).json({
      status: 'success',
      data: data,
    });
  });

export const getAll = <T extends Services>(ModelService: T) =>
  catchAsync(async (req: Request, res: Response, next: NextFunction) => {
    const data = await ModelService.getAll(req.query as QueryString);

    res.status(200).json({
      status: 'success',
      result: data.length,
      data: data,
    });
  });
