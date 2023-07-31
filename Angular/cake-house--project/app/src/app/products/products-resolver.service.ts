import { Injectable } from '@angular/core';
import {
  ActivatedRouteSnapshot,
  Resolve,
  RouterStateSnapshot,
} from '@angular/router';
import { ActivatedRoute } from '@angular/router';

import { Store } from '@ngrx/store';

import * as fromApp from '../store/app.reducer';
import { Actions, ofType } from '@ngrx/effects';
import { switchMap, take, of, Observable, catchError } from 'rxjs';
import { Product } from './product.model';
import * as ProductActions from './store/products.actions';

@Injectable({ providedIn: 'root' })
export class ProductsResolverService
  implements Resolve<{ product: Product | null }>
{
  slug: string;
  constructor(
    private store: Store<fromApp.AppStore>,
    private actions$: Actions
  ) {}
  resolve(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot
  ): Observable<{ product: Product | null }> {
    const productId = route.params['slug'];
    this.slug = productId;

    return this.store.select('products').pipe(
      take(1),
      switchMap((productsState) => {
        const products = productsState.products;
        if (!products || products.length === 0) {
          this.store.dispatch(ProductActions.loadingStart());
          return this.actions$.pipe(
            ofType(ProductActions.loadingSuccess),
            switchMap((action) => {
              const product = action.products?.find(
                (product) => product.slug === this.slug
              );
              return of({ product: product || null });
            }),
            catchError((error) => {
              return of({ product: error });
            })
          );
        } else {
          const product = productsState.products?.find(
            (product) => product.slug === this.slug
          );
          return of({ product: product });
        }
      })
    );
  }
}
