import express from 'express';

import userRouter from './routes/userRouter';

const app = express();
app.use(express.json());

app.use(express.urlencoded({ extended: false }));

app.use('/user', userRouter);

export default app;
