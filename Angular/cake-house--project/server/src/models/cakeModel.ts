import { Schema, model, Types, Document } from 'mongoose';
import slug from 'slug';

const startUrl = /^(https?:\/)?\/.*/i;

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
  ownerId?: Types.ObjectId;
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
          '8 peaces',
          '10 peaces',
          '12 peaces',
          '14 peaces',
          '16 peaces',
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
  ownerId: {
    type: Schema.Types.ObjectId,
    ref: 'User',
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
