import { createReducer, on } from '@ngrx/store';

import * as ProductsActions from '../store/products.actions';
import { Product } from '../product.model';
import { state } from '@angular/animations';

export interface State {
  products: Product[] | null ;
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

  on(ProductsActions.creatingStart, (state) => ({
    ...state,
    productError: null,
    loading: true,
  })),

  on(ProductsActions.createSuccess, (state, action) => ({
    ...state,
    productError: null,
    loading: false,
    products: [...action.products],
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
    products: state.products?.filter((product) => product.slug != action.slug) || null,
  })),
  
  on(ProductsActions.deleteProductSuccess, (state) => ({
    ...state,
    loading: false,
    productError: null
  }))
);
