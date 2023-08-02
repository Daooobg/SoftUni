import { Injectable } from '@angular/core';

import * as fromApp from '../store/app.reducer';
import { Store } from '@ngrx/store';

@Injectable({ providedIn: 'root' })
export class AuthService {
  constructor(private store: Store<fromApp.AppStore>) {}

  getUser() {
    return this.store.select('auth')
  }
}
