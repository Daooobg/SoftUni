import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { catchError, map, of, switchMap, tap } from 'rxjs';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { Router } from '@angular/router';

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
  constructor(
    private actions$: Actions,
    private http: HttpClient,
    private router: Router
  ) {}

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

  createProduct$ = createEffect(() =>
    this.actions$.pipe(
      ofType(ProductsActions.creatingStart),
      switchMap((action) => {
        return this.http
          .post<{data: Product, status: string}>(
            'http://localhost:5000/products/cakes',
            {
              product: action.product,
            },
            {
              headers: { Authorization: `Bear ${action.token}` },
            }
          )
          .pipe(
            map((productData) => {
              return ProductsActions.createSuccess({
                products: productData.data,
              });
            }),
            tap(() => this.router.navigate(['/products'])),
            catchError((errorRes) => {
              return handleError(errorRes);
            })
          );
      })
    )
  );

  editProduct$ = createEffect(() =>
    this.actions$.pipe(
      ofType(ProductsActions.editingStart),
      switchMap((action) => {
        console.log('slug',action.slug)
        return this.http
          .put<{data: Product, status: string}>(
            `http://localhost:5000/products/cakes/${action.slug}`,
            {
              product: action.product,
            },
            {
              headers: { Authorization: `Bear ${action.token}` },
            }
          )
          .pipe(
            map((productData) => {
              return ProductsActions.editSuccess({
                product: productData.data,
              });
            }),
            tap(() => this.router.navigate(['/products'])),
            catchError((errorRes) => {
              return handleError(errorRes);
            })
          );
      })
    )
  );

  deleteProduct = createEffect(() =>
    this.actions$.pipe(
      ofType(ProductsActions.deleteProduct),
      switchMap((action) => {
        console.log('action.token', action);
        return this.http
          .delete(`http://localhost:5000/products/cakes/${action.slug}`, {
            headers: { Authorization: `Bear ${action.token}` },
          })
          .pipe(
            map(() => {
              return ProductsActions.deleteProductSuccess();
            }),
            tap(() => this.router.navigate(['/products'])),
            catchError((errorRes) => {
              return handleError(errorRes);
            })
          );
      })
    )
  );
}
