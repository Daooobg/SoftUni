import mongoose, { ConnectOptions } from 'mongoose';
import dotenv from 'dotenv';

import app from './app';

process.on('uncaughtException', (err) => {
  console.log(err.name, err.message);
  console.log('UNCAUGHT EXCEPTION!!!! Shutting down....');

  process.exit(1);
});

dotenv.config({ path: 'config.env' });

const DB = process.env['DATABASE'] as string;


mongoose.set('strictQuery', false);
mongoose
  .connect(DB, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  } as  ConnectOptions)
  .then(() => {
    console.log('DB connected successfully!');
  });

const port: string = (process.env.PORT as string) || '5050';
const server = app.listen(port, () => {
  console.log(`App is running on port: ${port}`);
  
});

process.on('unhandledRejection', (err: Error) => {
  console.log(err.name, err.message);

  console.log('UNHANDLED REJECTION!!!! Shutting down....');
  server.close(() => {
    process.exit(1);
  });
});
