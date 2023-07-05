import dotenv from 'dotenv';
import jwt from '../lib/jsonwebtoken';
import catchAsync from '../utils/catchAsync';
import { Request, Response, NextFunction } from 'express';


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
