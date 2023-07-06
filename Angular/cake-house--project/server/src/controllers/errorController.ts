import { Request, Response, NextFunction } from 'express';
import { Error } from 'mongoose';
import { MongoError } from 'mongodb';
import AppError from '../utils/AppError';

interface AppErrorInterface extends Error {
  statusCode: number;
  status: string;
  isOperational: boolean;
  // code?: number
}

const sendError = (err: AppError, res: Response) => {
  if (err.isOperational) {
    res.status(err.statusCode).json({
      status: err.status,
      message: err.message,
    });
  } else {
    res.status(500).json({
      status: 'error',
      message: 'Something went very wrong!',
    });
  }
};

const handleCastError = (err: any) => {
  const message = `Invalid ${err.path}: ${err.value}.`;
  return new AppError(message, 400);
};

const handleValidationError = (err: Error.ValidationError) => {
  const errors = Object.values(err.errors).map((el: any) => el.message);
  const message = `Invalid input data: ${errors.join('. ')}`;
  return new AppError(message, 400);
};

const handleDuplicateFields = (err: MongoError) => {
  const value = err.message.match(/(["'])(\\?.)*?\1/);
  if (value) {
    const message = `Duplicate field value: (${value[0]}). Please use another value!`;
    return new AppError(message, 400);
  } else {
    return new AppError('Duplicate fields', 400);
  }
};

const handleTokenExpiredError = () =>
  new AppError('Your token has expired. Please log in again!', 401);

const handleJWTError = () =>
  new AppError('Invalid token. Please log in again!', 401);

const errorHandler = (
  err: AppErrorInterface,
  req: Request,
  res: Response,
  next: NextFunction
) => {
  err.statusCode = err.statusCode || 500;
  err.status = err.status || 'error';

  if (err instanceof Error.ValidationError) {
    err = handleValidationError(err as Error.ValidationError);
  }

  if (err.name === 'CastError') {
    err = handleCastError(err);
  }

  if (err instanceof MongoError && err.code === 11000) {
    err = handleDuplicateFields(err as MongoError); //TODO
  }

  if (err.name === 'TokenExpiredError') {
    err = handleTokenExpiredError();
  }

  if (err.name === 'JsonWebTokenError') {
    err = handleJWTError();
  }

  sendError(err as AppError, res as Response);
};

export default errorHandler;
