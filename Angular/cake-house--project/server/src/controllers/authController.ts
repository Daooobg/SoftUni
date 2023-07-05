import { Request, Response, NextFunction } from 'express';
import * as authService from '../services/authService';
import AppError from '../utils/AppError';
import catchAsync from '../utils/catchAsync';

export const register = catchAsync(
  async (
    req: Request,
    res: Response,
    next: NextFunction
  ): Promise<void | NextFunction> => {
    const { name, email, password, repeatPassword } = req.body;

    if (!email || !password || !repeatPassword || !name) {
      return next(new AppError('All fields are required', 400));
    }
    if (password !== repeatPassword) {
      return next(new AppError('Passwords do not match', 400));
    }
    const token = await authService.register(
      name,
      email,
      password,
      repeatPassword
    );

    res.status(200).json(token);
  }
);
