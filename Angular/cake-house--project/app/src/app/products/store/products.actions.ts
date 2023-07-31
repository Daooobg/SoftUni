import { createAction, props } from '@ngrx/store';

import { Product } from '../product.model';

export const loadingStart = createAction('[Products] Loading Start');
export const creatingStart = createAction(
  '[Products] Creating Start',
  props<{ product: Product; token: string | null }>()
);

export const loadingSuccess = createAction(
  '[Products] Products Loading Success',
  props<{
    products: Product[];
  }>()
);

export const loadingFail = createAction(
  '[Products] Products Loading Fail',
  props<{
    errorMessage: string;
  }>()
);

export const createSuccess = createAction(
  '[Products] Products Create Success',
  props<{ products: Product[] }>()
);
