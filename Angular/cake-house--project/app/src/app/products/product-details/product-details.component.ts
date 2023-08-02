import { Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { Product } from '../product.model';
import { Store } from '@ngrx/store';

import * as fromApp from '../../store/app.reducer';
import * as productsActions from '../store/products.actions';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-product-details',
  templateUrl: './product-details.component.html',
  styleUrls: ['./product-details.component.css'],
})
export class ProductDetailsComponent implements OnInit, OnDestroy {
  token: string | null = JSON.parse(localStorage.getItem('userData')!)
    ?.AccessToken;
  product: Product | any;
  error: string;
  activeImg: string;
  activeSize: string;
  price: number;

  isLoading: boolean = false;
  errorOnDelete: string | null = null;

  productSub: Subscription;

  constructor(
    private route: ActivatedRoute,
    private store: Store<fromApp.AppStore>
  ) {}
  ngOnInit(): void {
    this.route.data.subscribe((data: any) => {
      this.product = data[0].product as Product | null;
    });
    this.setActiveImg(0);
    this.setActiveSize(this.product.sizes[0]);
    if (!this.product) {
      this.error = 'Something went wrong';
    }

    this.productSub = this.store.select('products').subscribe((product) => {
      this.isLoading = product.loading;
      this.errorOnDelete = product.productError;
    });
  }

  setActiveImg(i: number) {
    this.activeImg = this.product.images[i];
  }

  setActiveSize(size: string) {
    this.activeSize = size;
    if (this.activeSize) {
      this.price = +this.activeSize.slice(0, 2) * this.product.price;
    }
  }

  onDelete() {
    this.store.dispatch(
      productsActions.deleteProduct({
        slug: this.product.slug,
        token: this.token,
      })
    );
  }

  ngOnDestroy(): void {
    this.productSub.unsubscribe();
  }
}
