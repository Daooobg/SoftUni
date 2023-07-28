import * as fromAuth from '.././auth/store/auth.reducer';

export interface AppStore {
  auth: fromAuth.State;
}
