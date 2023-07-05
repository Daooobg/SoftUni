import mongoose, { Model, UpdateQuery } from 'mongoose';
import slug from 'slug';

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

export const updateOne =
  <T extends IProduct>(Model: Model<T>) =>
  async (slugData: string, data: UpdateQuery<T>): Promise<T | null> => {
    if (data.name) {
      data.slug = slug(`${data.name}`, {
        lower: true,
      });
    }
    const result = await Model.findOneAndUpdate({ slug: slugData }, data, {
      new: true,
      runValidators: true,
    });
    return result;
  };
