import { Schema, model, Types, Document } from 'mongoose';
import slug from 'slug';

const startUrl = /^(https?:\/)?\/.*/i;
interface Comment {
  ownerId: Types.ObjectId;
  comment: string;
  rating: number;
}
export interface ICake extends Document {
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
  ownerId?: Types.ObjectId;
  averageRating?: Number;
}

const cakeSchema = new Schema<ICake>({
  name: {
    type: String,
    lowercase: true,
    required: [true, 'Please provide name'],
    minLength: [3, 'Name must be at least 3 characters'],
    unique: true,
  },
  product: {
    type: String,
    default: 'cakes',
  },
  types: [
    {
      type: String,
      enum: {
        values: [
          'fruit',
          'vegetable',
          'mixed',
          'chocolate',
          'dairy-free',
          'keto',
          'nut-free',
          'probiotic',
          'kids',
        ],
        message:
          'Cake types are fruit, vegetable, mixed, chocolate, dairy-free, keto, nut-free, probiotic, and kids',
      },
    },
  ],
  sizes: [
    {
      type: String,
      enum: {
        values: [
          '8 Pieces',
          '10 Pieces',
          '12 Pieces',
          '14 Pieces',
          '16 Pieces',
        ],
        message: 'Cake sizes must be 8, 10, 12, 14, and 16 peaces',
      },
    },
  ],
  description: {
    type: String,
    required: [true, 'Please provide description'],
    minLength: [10, 'Description must be at least 10 characters'],
  },
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
  images: [
    {
      type: String,
      validate: {
        validator: (value: string) => startUrl.test(value),
        message: `Please add valid image URL`,
      },
    },
  ],
  price: {
    type: Number,
    required: [true, 'Please provide price'],
    min: [0, 'Cake price must be a positive number'],
  },
  priceDiscount: {
    type: Number,
    default: 0,
  },
  createdAt: {
    type: Date,
    default: Date.now(),
  },
  slug: String,
  comments: [
    {
      ownerId: {
        type: Schema.Types.ObjectId,
        ref: 'User',
      },
      comment: {
        type: String,
      },
      rating: {
        type: Number,
      },
    },
  ],
  ownerId: {
    type: Schema.Types.ObjectId,
    ref: 'User',
  },
  averageRating: {
    type: Number,
    default: 0,
  },
});

cakeSchema.pre<ICake>('save', function (next) {
  this.slug = slug(`${this.name}`, {
    lower: true,
  });
  next();
});

const Cake = model<ICake>('Cake', cakeSchema);

export default Cake;
