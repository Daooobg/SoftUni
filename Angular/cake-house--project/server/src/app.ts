import express, { ErrorRequestHandler } from 'express';

import userRouter from './routes/userRouter';
import errorHandler from './controllers/errorController';

const app = express();
app.use(express.json());

app.use(express.urlencoded({ extended: false }));

app.use('/user', userRouter);

app.use(errorHandler as ErrorRequestHandler);
export default app;
