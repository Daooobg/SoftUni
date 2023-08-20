import { createAction, props } from '@ngrx/store';
import { ShoppingProduct } from 'src/app/shopping/shopping.model';

export const loginStart = createAction(
  '[Auth] Login Start',
  props<{
    email: string;
    password: string;
  }>()
);

export const signupStart = createAction(
  '[Auth] Signup Start',
  props<{
    username: string;
    email: string;
    password: string;
    repPassword: string;
  }>()
);

export const authenticateSuccess = createAction(
  '[Auth] Authenticate Success',
  props<{
    username: string;
    email: string;
    userId: string;
    role: string;
    AccessToken: string;
    redirect: boolean;
  }>()
);

export const authenticateFail = createAction(
  '[Auth] Authenticate Fail',
  props<{
    errorMessage: string;
  }>()
);

export const clearError = createAction('[Auth] Clear Error');

export const autoLogin = createAction('[Auth] Auto Login');

export const logout = createAction('[Auth] Logout');

export const shoppingBag = createAction(
  '[Auth] Add to shopping bag',
  props<{
    product: ShoppingProduct;
  }>()
);

export const buyProducts = createAction('[Auth] Buy products')