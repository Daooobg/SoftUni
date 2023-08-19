import { createReducer, on } from '@ngrx/store';

import * as ProductsActions from '../store/products.actions';
import { Product } from '../product.model';

export interface State {
  products: Product[] | null;
  productError: string | null;
  loading: boolean;
}

const initialState: State = {
  products: null,
  productError: null,
  loading: false,
};

export const productsReducer = createReducer(
  initialState,

  on(ProductsActions.creatingStart, ProductsActions.editingStart, (state) => ({
    ...state,
    productError: null,
    loading: true,
  })),

  on(ProductsActions.createSuccess, (state, action) => ({
    ...state,
    productError: null,
    loading: false,
    products: (state.products ?? []).concat(action.products),
  })),

  on(ProductsActions.editSuccess, (state, action) => ({
    ...state,
    productError: null,
    loading: false,
    products:
      state.products?.map((product) =>
        product._id === action.product._id ? { ...action.product } : product
      ) ?? null,
  })),

  on(ProductsActions.loadingStart, (state) => ({
    ...state,
    productError: null,
    loading: true,
  })),

  on(ProductsActions.loadingSuccess, (state, action) => ({
    ...state,
    productError: null,
    loading: false,
    products: [...action.products],
  })),

  on(ProductsActions.loadingFail, (state, action) => ({
    ...state,
    productError: action.errorMessage,
    loading: false,
  })),

  on(ProductsActions.deleteProduct, (state, action) => ({
    ...state,
    loading: true,
    productError: null,
    products:
      state.products?.filter((product) => product.slug != action.slug) || null,
  })),

  on(ProductsActions.deleteProductSuccess, (state) => ({
    ...state,
    loading: false,
    productError: null,
  })),

  on(ProductsActions.createComment, (state, action) => ({
    ...state,
    products: state.products!.map((product) => {
      if (product.slug === action.slug) {
        const newComment = {
          rating: +action.comment.rating,
          comment: action.comment.comment,
          ownerId: { _id: action.ownerId._id, name: action.ownerId.name },
        };
        const updatedComments = product.comments
          ? [...product.comments, newComment]
          : [newComment];
        let rating = 0;
        if (product.comments && product.averageRating) {
          rating =
            (+product.averageRating * product.comments.length +
              +action.comment.rating) /
            (product.comments.length + 1);
        } else {
          rating = +action.comment.rating;
        }
        return { ...product, comments: updatedComments, averageRating: rating };
      }
      return product;
    }),
  }))
);
