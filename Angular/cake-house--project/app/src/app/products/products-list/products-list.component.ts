import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subscription, map } from 'rxjs';
import { Store } from '@ngrx/store';

import * as fromApp from '../../store/app.reducer';
import * as productsActions from '../store/products.actions';
import { Product } from '../product.model';

@Component({
  selector: 'app-products-list',
  templateUrl: './products-list.component.html',
  styleUrls: ['./products-list.component.css'],
})
export class ProductsListComponent implements OnInit, OnDestroy {
  products: Product[] | null;
  error: string | null = null;
  isLoading: boolean = false;
  isAuthenticated = false;
  role: string | undefined;

  productsSub: Subscription;
  userSub: Subscription;

  constructor(private store: Store<fromApp.AppStore>) {}

  ngOnInit(): void {
    // this.store.dispatch(productsActions.loadingStart());
    this.productsSub = this.store
      .select('products')
      .subscribe((productsData) => {
        this.isLoading = productsData.loading;
        this.products = productsData.products;
        this.error = productsData.productError;
      });
    this.userSub = this.store
      .select('auth')
      .pipe(map((authState) => authState.user))
      .subscribe((user) => {
        this.isAuthenticated = !!user;
        this.role = user?.role;
      });
  }

  ngOnDestroy(): void {
    this.productsSub.unsubscribe();
    this.userSub.unsubscribe();
  }
}
