import dotenv from 'dotenv';
import jwt from '../lib/jsonwebtoken';
import catchAsync from '../utils/catchAsync';
import { Request, Response, NextFunction } from 'express';
import AppError from '../utils/AppError';

dotenv.config({ path: './config.env' });

const SECRET = process.env.JWT_SECRET;

export const authentication = catchAsync(
  async (req: Request, res: Response, next: NextFunction) => {
    if (req.header?.('Authorization')) {
      const token = req.header('Authorization')?.split(' ')[1];
      if (token) {
        if (SECRET) {
          const decodedToken = await jwt.verify(token, SECRET);
          req.user = decodedToken;
        }
      }
    }

    next();
  }
);

export const restrictTo = (...roles: string[]) => {
  return (req: Request, res: Response, next: NextFunction): void => {
    if (!req.user) {
      return next(new AppError('You are not logged in', 403));
    }
    if (req.user.role && !roles.includes(req.user.role)) {
      return next(
        new AppError('You do not have permission to perform this action', 403)
      );
    }
    next();
  };
};
