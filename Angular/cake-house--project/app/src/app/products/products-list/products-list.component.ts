import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { Store } from '@ngrx/store';

import * as fromApp from '../../store/app.reducer';
import { Product } from '../product.model';
import { AuthService } from 'src/app/auth/auth.service';
import { User } from 'src/app/auth/user.model';

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
  user: User | null;
  productsSub: Subscription;
  userSub: Subscription;

  constructor(
    private store: Store<fromApp.AppStore>,
    private authService: AuthService
  ) {}

  ngOnInit(): void {
    this.productsSub = this.store
      .select('products')
      .subscribe((productsData) => {
        this.isLoading = productsData.loading;
        this.products = productsData.products;
        this.error = productsData.productError;
      });
    this.authService.getUser().subscribe((authData) => {
      if (authData.user?.role) {
        this.isAuthenticated = !!authData.user;
        this.role = authData.user.role;
      }
    });
  }

  ngOnDestroy(): void {
    this.productsSub.unsubscribe();
  }
}
