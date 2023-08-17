import mongoose, { Model, UpdateQuery } from 'mongoose';
import slug from 'slug';

import { APIFeatures, QueryString } from '../utils/ApiFeatures';
import { ICake } from '../models/cakeModel';

interface Comment {
  ownerId: mongoose.Types.ObjectId;
  comment: string;
  rating: number;
}
interface IProduct {
  name: string;
  product: string;
  types: string[];
  sizes: string[];
  description: string;
  logoDescription: string[];
  images: string[];
  price: number;
  priceDiscount: number;
  createdAt: Date;
  slug: string;
  comments?: Comment[];
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

export const createComment =
  <T extends ICake>(Model: Model<T>) =>
  async (
    data: UpdateQuery<T>,
    userId: mongoose.Types.ObjectId
  ): Promise<T | null> => {
    const product = await Model.findOne({ slug: data.slug });
    if (product?.comments) {
      const userComment = product.comments.find(
        (comment) => comment.ownerId.toString() === userId.toString()
      );
      if (userComment) {
        return null;
      }
    }
    const comment = await Model.findOneAndUpdate(
      { slug: data.slug },
      {
        $push: {
          comments: {
            ownerId: userId,
            comment: data.comment,
            rating: data.rating,
          },
        },
      }
    );
    return comment;
  };

export const deleteOne =
  <T extends IProduct>(Model: Model<T>) =>
  async (slugData: string): Promise<T | null> => {
    if (!slugData) {
      return null;
    }

    return await Model.findOneAndDelete({ slug: slugData });
  };
