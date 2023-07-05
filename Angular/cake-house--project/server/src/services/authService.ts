import User from '../models/userModel';
import dotenv from 'dotenv';
import jwt from '../lib/jsonwebtoken';


dotenv.config({ path: './config.env' });

const SECRET = process.env.JWT_SECRET;
const EXPIRES_IN = process.env.JWT_EXPIRES_IN;

const createAndSendToken = async (user: {
  name: string;
  email: string;
  _id: string;
  role: string;
}) => {
  const payload = {
    name: user.name,
    email: user.email,
    _id: user._id,
    role: user.role,
  };
  if (SECRET && EXPIRES_IN) {
    const token = await jwt.sign(payload, SECRET, { expiresIn: EXPIRES_IN });

    const response = {
      AccessToken: token,
      name: user.name,
      email: user.email,
      userId: user._id,
    };
    return response;
  }
};

export const register = async (
  name: string,
  email: string,
  password: string,
  repeatPassword: string
) => {
  const user = await User.create({ name, email, password, repeatPassword });
  return createAndSendToken(user);
};