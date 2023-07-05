import { Schema, Model, Document, Types, model } from 'mongoose';
import slug from 'slug';

const startUrl = /^(https?:\/)?\/.*/i;

export interface ICandy extends Document {
  name: string;
  price: number;
  boxSize: number[];
  priceDiscount?: number;
  images?: string[];
  logoDescription?: string[];
  createdAt: Date;
  slug?: string;
  ownerId: Types.ObjectId;
}

export interface ICandyModel extends Model<ICandy> {}

const candySchema = new Schema<ICandy>({
  name: {
    type: String,
    lowercase: true,
    required: [true, 'Please provide name'],
    minLength: [3, 'Name must be at least 3 characters'],
    unique: true,
    trim: true,
  },
  price: {
    type: Number,
    required: [true, 'Please provide price'],
    min: [0, 'Price must be a positive number'],
  },
  boxSize: [
    {
      type: Number,
      min: [1, 'Box size must be minimum 1'],
    },
  ],
  priceDiscount: {
    type: Number,
    default: 0,
  },
  images: [
    {
      type: String,
      validate: {
        validator: (value: string) => startUrl.test(value),
        message: `Please add valid image URL`,
      },
    },
  ],
  logoDescription: [
    {
      type: String,
      enum: [
        'glutenFree',
        'sugarFree',
        'vegan',
        'keto',
        'paleo',
        'dairyFree',
        'nutFree',
        'soyFree',
        'diabetics',
        'probiotics',
      ],
    },
  ],
  createdAt: {
    type: Date,
    default: Date.now,
  },
  slug: String,
  ownerId: {
    type: Schema.Types.ObjectId,
    ref: 'User',
  },
});

candySchema.pre('save', function (next) {
  this.slug = slug(`${this.name}`, {
    lower: true,
  });
  next();
});

const Candy = model<ICandy>('Candy', candySchema);

export default Candy;
