import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { catchError, map, of, switchMap } from 'rxjs';
import { Actions, createEffect, ofType } from '@ngrx/effects';

import * as ProductsActions from './products.actions';
import { Product } from '../product.model';

export interface ProductsResponseData {
  status: string;
  result: number;
  data: Product[];
}

const handleError = (errorRes: any) => {
  let errorMessage = 'An unknown error occurred!';
  if (errorRes.error.message) {
    errorMessage = errorRes.error.message;
  }
  return of(ProductsActions.loadingFail({ errorMessage }));
};

@Injectable()
export class ProductsEffects {
  constructor(private actions$: Actions, private http: HttpClient) {}

  loadingProducts$ = createEffect(() =>
    this.actions$.pipe(
      ofType(ProductsActions.loadingStart),
      switchMap(() => {
        return this.http.get<ProductsResponseData>(
          'http://localhost:5000/products/cakes'
        );
      }),
      map((products) => {
        return products.data;
      }),
      map((products) => {
        return ProductsActions.loadingSuccess({ products });
      }),
      catchError((errorRes) => {
        return handleError(errorRes);
      })
    )
  );
}
