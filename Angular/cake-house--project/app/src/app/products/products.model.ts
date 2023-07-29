import { NgModule } from '@angular/core';
import { StoreModule } from '@ngrx/store';

import * as fromProducts from './store/products.reducer';


@NgModule({
  declarations: [],
  imports: [StoreModule.forFeature('products', fromProducts.productsReducer)],
})
export class ProductsModule {}
