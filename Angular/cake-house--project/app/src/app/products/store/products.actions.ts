import { createAction, props } from '@ngrx/store';

import { Product } from '../product.model';

export const loadingStart = createAction('[Products] Loading Start');

export const loadingSuccess = createAction(
  '[Products] Products Loading Success',
  props<{
    products: Product[]
  }>()
);

export const loadingFail = createAction(
    '[Products] Products Loading Fail',
    props<{
      errorMessage: string;
    }>()
  );