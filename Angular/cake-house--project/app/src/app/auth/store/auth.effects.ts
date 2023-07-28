import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Actions, ofType, createEffect } from '@ngrx/effects';
import { switchMap, catchError, map, tap } from 'rxjs/operators';
import { of } from 'rxjs';
import { HttpClient } from '@angular/common/http';

import * as AuthActions from './auth.actions';
import { User } from '../user.model';

export interface AuthResponseData {
  username: string;
  email: string;
  userId: string;
  role: string;
  AccessToken: string;
}

const handleAuthentication = (
  username: string,
  email: string,
  userId: string,
  role: string,
  AccessToken: string
) => {
  const user = new User(username, email, userId, role, AccessToken);
  localStorage.setItem('userData', JSON.stringify(user));
  return AuthActions.authenticateSuccess({
    username,
    email,
    userId,
    role,
    AccessToken,
    redirect: true,
  });
};

const handleError = (errorRes: any) => {
  let errorMessage = 'An unknown error occurred!';
  if (errorRes.error.message) {
    errorMessage = errorRes.error.message;
  }
  return of(AuthActions.authenticateFail({ errorMessage }));
};

@Injectable()
export class AuthEffects {
  constructor(
    private actions$: Actions,
    private http: HttpClient,
    private router: Router // private authService: AuthService
  ) {}

  authSignup$ = createEffect(() =>
    this.actions$.pipe(
      ofType(AuthActions.signupStart),
      switchMap((action) => {
        return this.http
          .post<AuthResponseData>('http://localhost:5000/user/register', {
            name: action.username,
            email: action.email,
            password: action.password,
            repeatPassword: action.repPassword,
          })
          .pipe(
            map((resData) => {
              console.log('resData', resData);
              return handleAuthentication(
                resData.username,
                resData.email,
                resData.userId,
                resData.role,
                resData.AccessToken
              );
            }),
            catchError((errorRes) => {
              return handleError(errorRes);
            })
          );
      })
    )
  );

  authLogin$ = createEffect(() =>
    this.actions$.pipe(
      ofType(AuthActions.loginStart),
      switchMap((action) => {
        return this.http
          .post<AuthResponseData>('http://localhost:5000/user/login', {
            email: action.email,
            password: action.password,
          })
          .pipe(
            map((resData) => {
              return handleAuthentication(
                resData.username,
                resData.email,
                resData.userId,
                resData.role,
                resData.AccessToken
              );
            }),
            catchError((errorRes) => {
              return handleError(errorRes);
            })
          );
      })
    )
  );

  authRedirect$ = createEffect(
    () =>
      this.actions$.pipe(
        ofType(AuthActions.authenticateSuccess),
        tap((action) => action.redirect && this.router.navigate(['/']))
      ),
    { dispatch: false }
  );

  autoLogin$ = createEffect(() =>
    this.actions$.pipe(
      ofType(AuthActions.autoLogin),
      map(() => {
        const userData: {
          username: string;
          email: string;
          userId: string;
          role: string;
          AccessToken: string;
        } = JSON.parse(localStorage.getItem('userData')!);
        if (!userData) {
          return { type: 'DUMMY' };
        }
        console.log('userData', userData);
        const loadedUser = new User(
          userData.username,
          userData.email,
          userData.userId,
          userData.role,
          userData.AccessToken
        );
        console.log('loadedUser', loadedUser);
        if (loadedUser.token) {
          return AuthActions.authenticateSuccess({
            username: loadedUser.username,
            email: loadedUser.email,
            userId: loadedUser.userId,
            role: loadedUser.role,
            AccessToken: loadedUser.token,
            redirect: false,
          });
        }
        return { type: 'DUMMY' };
      })
    )
  );
}
