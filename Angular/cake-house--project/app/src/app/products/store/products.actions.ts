import { createAction, props } from '@ngrx/store';

import { Product } from '../product.model';

export const loadingStart = createAction('[Products] Loading Start');
export const creatingStart = createAction(
  '[Products] Creating Start',
  props<{ product: Product; token: string | null }>()
);
export const editingStart = createAction(
  '[Products] Editing Start',
  props<{ product: Product; token: string | null; slug: string | null;  }>()
);

export const loadingSuccess = createAction(
  '[Products] Products Loading Success',
  props<{
    products: Product[];
  }>()
);

export const editingSuccess = createAction(
  '[Products] Products Editing Success',
  props<{
    product: Product;
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
  props<{ products: Product }>()
);

export const editSuccess = createAction(
  '[Products] Product Edit Success',
  props<{ product: Product }>()
);

export const deleteProduct = createAction(
  '[Products] Delete Product',
  props<{ slug: string; token: string | null }>()
);

export const deleteProductSuccess = createAction(
  '[Products] Delete Product Success'
);
