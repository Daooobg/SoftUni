import { Types, UpdateQuery } from 'mongoose';
import { NextFunction, Request, Response } from 'express';

import catchAsync from '../utils/catchAsync';
import AppError from '../utils/AppError';
import { QueryString } from '../utils/ApiFeatures';

interface Services {
  createOne: (data: {}, objectId: Types.ObjectId) => Promise<object | null>;
  getAll: (query: QueryString) => Promise<object[]>;
  updateOne: <T>(slug: string, data: UpdateQuery<T>) => {};
  deleteOne: (slug: string) => Promise<object | null>;
}

export const createOne = <T extends Services>(ModelService: T) =>
  catchAsync(async (req: Request, res: Response, next: NextFunction) => {
    const userId = req.user?._id;
    if (!userId) {
      return next(new AppError('Please Login!', 401));
    }

    const objectId = new Types.ObjectId(userId);

    const data = await ModelService.createOne(req.body.product, objectId);

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

export const updateOne = <T extends Services>(ModelService: T) =>
  catchAsync(async (req: Request, res: Response, next: NextFunction) => {
    
    const data = await ModelService.updateOne(req.params.slug, req.body.product);

    if (!data) {
      return next(new AppError(`No data found for: ${req.params.slug}`, 404));
    }

    res.status(200).json({
      status: 'success',
      data: data,
    });
  });

export const deleteOne = <T extends Services>(ModelService: T) =>
  catchAsync(async (req: Request, res: Response, next: NextFunction) => {
    const data = await ModelService.deleteOne(req.params.slug);

    if (!data) {
      return next(new AppError(`No data found for: ${req.params.slug}`, 404));
    }

    res.status(204).json({
      status: 'success',
      data: null,
    });
  });
