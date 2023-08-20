import { createReducer, on } from '@ngrx/store';
import { User } from '../user.model';
import * as AuthActions from './auth.actions';
import { ShoppingProduct } from 'src/app/shopping/shopping.model';

export interface State {
  user: User | null;
  authError: string | null;
  loading: boolean;
  products: ShoppingProduct[];
}

const initialState: State = {
  user: null,
  authError: null,
  loading: false,
  products: [],
};

export const authReducer = createReducer(
  initialState,

  on(AuthActions.loginStart, AuthActions.signupStart, (state) => ({
    ...state,
    authError: null,
    loading: true,
  })),

  on(AuthActions.authenticateSuccess, (state, action) => ({
    ...state,
    authError: null,
    loading: false,
    user: new User(
      action.username,
      action.email,
      action.userId,
      action.role,
      action.AccessToken
    ),
  })),

  on(AuthActions.authenticateFail, (state, action) => ({
    ...state,
    user: null,
    authError: action.errorMessage,
    loading: false,
  })),

  on(AuthActions.logout, (state) => ({
    ...state,
    user: null,
  })),

  on(AuthActions.clearError, (state) => ({
    ...state,
    authError: null,
  })),
  on(AuthActions.logout, (state) => ({
    ...state,
    user: null,
  })),
  on(AuthActions.shoppingBag, (state, action) => ({
    ...state,
    products: [...state.products, action.product],
  })),
  on(AuthActions.buyProducts, (state) => ({
    ...state,
    products: [],
  }))
);
