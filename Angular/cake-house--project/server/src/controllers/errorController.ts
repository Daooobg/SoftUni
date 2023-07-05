import { Request, Response, NextFunction } from 'express';
import AppError from '../utils/AppError';

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

const handleValidationError = (err: any) => {
  const errors = Object.values(err.errors).map((el: any) => el.message);
  const message = `Invalid input data: ${errors.join('. ')}`;
  return new AppError(message, 400);
};

const handleDuplicateFields = (err: any) => {
  const value = err.errmsg.match(/(["'])(\\?.)*?\1/)[0];
  const message = `Duplicate field value: (${value}). Please use another value!`;
  return new AppError(message, 400);
};

const handleTokenExpiredError = () =>
  new AppError('Your token has expired. Please log in again!', 401);

const handleJWTError = () =>
  new AppError('Invalid token. Please log in again!', 401);

const errorHandler = (
  err: any,
  req: Request,
  res: Response,
  next: NextFunction
) => {
  err.statusCode = err.statusCode || 500;
  err.status = err.status || 'error';

  if (err.name === 'ValidationError') {
    err = handleValidationError(err);
  }

  if (err.name === 'CastError') {
    err = handleCastError(err);
  }

  if (err.code === 11000) {
    err = handleDuplicateFields(err); //TODO
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
