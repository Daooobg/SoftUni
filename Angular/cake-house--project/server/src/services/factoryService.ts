import mongoose, { Model } from 'mongoose';

interface IProduct {
  name?: string;
  ownerId?: mongoose.Types.ObjectId;
}

export const createOne =
  <T extends IProduct>(Model: Model<T>) =>
  async (data: Partial<T>, userId: mongoose.Types.ObjectId): Promise<T> => {
    data.ownerId = userId;
    return await Model.create(data);
  };