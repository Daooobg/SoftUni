import { Schema, Document, model } from 'mongoose';
import bcrypt from 'bcrypt';
import validator from 'validator';

export interface IUser extends Document {
  name: string;
  email: string;
  password: string;
  role: 'user' | 'owner' | 'driver' | 'admin';
  address: {
    phoneNumber: string;
    firstLine: string;
    secondLine?: string;
    city: string;
    county: string;
    postcode: string;
  };
  shippingAddress?: {
    phoneNumber: string;
    firstLine: string;
    secondLine?: string;
    city: string;
    county: string;
    postcode: string;
  };
  validatePassword(password: string): Promise<boolean>;
}

const userSchema = new Schema<IUser>({
  name: {
    type: String,
    lowercase: true,
    required: [true, 'Please tell us your name'],
    minlength: [3, 'Name must have more or equal than 3 characters'],
  },
  email: {
    type: String,
    lowercase: true,
    unique: true,
    required: [true, 'Please tell us your email'],
    validate: [validator.isEmail, 'Please provide a valid email'],
  },
  password: {
    type: String,
    required: [true, 'Please tell us your password'],
    minlength: [6, 'Password must have more or equal than 6 characters'],
  },
  role: {
    type: String,
    enum: ['user', 'owner', 'driver', 'admin'],
    default: 'user',
  },
  address: {
    phoneNumber: {
      type: String,
      min: [8, 'Phone number must be at least 8 numbers'],
    },
    firstLine: {
      type: String,
      minlength: [4, 'Address must have more or equal than 4 characters'],
    },
    secondLine: {
      type: String,
    },
    city: {
      type: String,
      minlength: [2, 'City must have more or equal than 2 characters'],
    },
    county: {
      type: String,
      minlength: [2, 'County must have more or equal than 2 characters'],
    },
    postcode: {
      type: String,
      minlength: [6, 'Postcode must have more or equal than 6 characters'],
    },
  },
  shippingAddress: {
    phoneNumber: {
      type: String,
      min: [8, 'Phone number must be at least 8 numbers'],
    },
    firstLine: {
      type: String,
      minlength: [4, 'Address must have more or equal than 4 characters'],
    },
    secondLine: {
      type: String,
    },
    city: {
      type: String,
      minlength: [2, 'City must have more or equal than 2 characters'],
    },
    county: {
      type: String,
      minlength: [2, 'County must have more or equal than 2 characters'],
    },
    postcode: {
      type: String,
      minlength: [6, 'Postcode must have more or equal than 6 characters'],
    },
  },
});

userSchema.pre<IUser>('save', async function (next) {
  const hash = await bcrypt.hash(this.password, 10);
  this.password = hash;
  next();
});

userSchema.methods.validatePassword = function (password: string): Promise<boolean> {
  return bcrypt.compare(password, this.password);
};

const User = model<IUser>('User', userSchema);

export default User;
