import { RequestHandler } from 'express';

declare module 'express' {
  interface Request {
    user: {
      _id?: string;
      role?: string;
      name?: string;
      email?: string;
      // Add other properties of the user object
    };
  }
}


const catchAsync = (fn: Function): RequestHandler => {
  return (req, res, next) => {
    fn(req, res, next).catch(next);
  };
};

export default catchAsync;
