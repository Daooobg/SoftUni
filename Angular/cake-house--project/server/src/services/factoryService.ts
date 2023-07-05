import mongoose, { Model } from 'mongoose';

import { APIFeatures, QueryString } from '../utils/ApiFeatures';

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

export const getAll =
  <T extends IProduct>(Model: Model<T>) =>
  async (queryData: QueryString) => {
    const feature = new APIFeatures(Model.find(), queryData)
      .filter()
      .sort()
      .limitFields()
      .paginate();
    return (await feature.query) as object[];
  };
