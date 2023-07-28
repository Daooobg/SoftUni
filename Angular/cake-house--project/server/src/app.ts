import express, { ErrorRequestHandler } from 'express';
import cors from 'cors';

import userRouter from './routes/userRouter';
import productsRouter from './routes/productsRouter';
import errorHandler from './controllers/errorController';
import { authentication } from './middlewares/authMiddleware';

const app = express();
app.use(cors());

app.use(express.urlencoded({ extended: false }));

app.use(express.json());


app.use(authentication);

app.use('/user', userRouter);
app.use('/products/', productsRouter);

app.use(errorHandler as ErrorRequestHandler);
export default app;
