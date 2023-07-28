import { Component, OnDestroy, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Store } from '@ngrx/store';
import * as AuthActions from './store/auth.actions';

import * as fromApp from '../store/app.reducer';
import { Subscription } from 'rxjs';
@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.css'],
})
export class AuthComponent implements OnInit, OnDestroy {
  isVisible = false;
  isLogin = true;
  isLoading = false;
  error: string | null = null;

  storeSub!: Subscription;

  constructor(private store: Store<fromApp.AppStore>) {}

  ngOnInit(): void {
    this.storeSub = this.store.select('auth').subscribe((data) => {
      console.log('subs', data);
      this.isLoading = data.loading;
      this.error = data.authError;
    });
  }

  onChangeVisibility() {
    this.isVisible = !this.isVisible;
  }

  onChangeForm() {
    this.isLogin = !this.isLogin;
    this.error = null
  }

  onSubmit(form: NgForm) {
    const email = form.value.email;
    const password = form.value.password;

    if (this.isLogin) {
      this.store.dispatch(AuthActions.loginStart({ email, password }));
    } else {
      const username = form.value.username;
      const repPassword = form.value.repPassword;
      this.store.dispatch(
        AuthActions.signupStart({ username, email, password, repPassword })
      );
    }
  }

  ngOnDestroy(): void {
    this.storeSub.unsubscribe();
  }
}
