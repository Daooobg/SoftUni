import * as fromAuth from '.././auth/store/auth.reducer';
import * as fromProducts from '../products/store/products.reducer';
export interface AppStore {
  auth: fromAuth.State;
  products: fromProducts.State;
}
