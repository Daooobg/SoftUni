import { Component, OnInit } from '@angular/core';
import { Store } from '@ngrx/store';
import { Subscription } from 'rxjs';

import * as fromApp from '../store/app.reducer';
import { ShoppingProduct } from './shopping.model';
import * as AuthActions from '../auth/store/auth.actions';

@Component({
  selector: 'app-shopping',
  templateUrl: './shopping.component.html',
  styleUrls: ['./shopping.component.css'],
})
export class ShoppingComponent implements OnInit {
  shoppingProducts: ShoppingProduct[];
  shoppingSub: Subscription;
  totalPrice: number;
  isBought: boolean = false;

  constructor(private store: Store<fromApp.AppStore>) {}

  ngOnInit(): void {
    this.shoppingSub = this.store.select('auth').subscribe((data) => {
      this.shoppingProducts = data.products;
      this.totalPrice = data.products.reduce(
        (sum, product) => sum + product.price,
        0
      );
    });
  }

  onBuy() {
    this.store.dispatch(AuthActions.buyProducts());
    this.isBought = true;
  }
}
