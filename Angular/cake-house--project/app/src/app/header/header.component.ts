import { Component, OnDestroy, OnInit } from '@angular/core';
import { Store } from '@ngrx/store';
import { Subscription, map } from 'rxjs';

import * as fromApp from '../store/app.reducer';
import { User } from '../auth/user.model';
import * as AuthActions from '../auth/store/auth.actions';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css'],
})
export class HeaderComponent implements OnInit, OnDestroy {
  isAuthenticated = false;
  private userSubs!: Subscription;
  user!: User | null;

  constructor(private store: Store<fromApp.AppStore>) {}
  ngOnInit(): void {
    this.userSubs = this.store
      .select('auth')
      .pipe(map((authState) => authState.user))
      .subscribe((user) => {
        this.isAuthenticated = !!user;
      });
  }
  ngOnDestroy(): void {
    this.userSubs.unsubscribe();
  }

  onLogout() {
    localStorage.removeItem('userData');
    this.store.dispatch(AuthActions.logout());
  }
}
