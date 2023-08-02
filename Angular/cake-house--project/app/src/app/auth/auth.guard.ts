import {
  CanActivate,
  ActivatedRouteSnapshot,
  RouterStateSnapshot,
  Router,
  UrlTree,
} from '@angular/router';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map, take } from 'rxjs/operators';
import { Store } from '@ngrx/store';

import * as fromApp from '../store/app.reducer';

@Injectable({ providedIn: 'root' })
export class AuthGuard implements CanActivate {
  user: string[];
  constructor(private router: Router, private store: Store<fromApp.AppStore>) {}

  setUser(user: string[]): void {
    this.user = user;
  }

  canActivate(
    route: ActivatedRouteSnapshot,
    router: RouterStateSnapshot
  ):
    | boolean
    | UrlTree
    | Promise<boolean | UrlTree>
    | Observable<boolean | UrlTree> {
    this.user = route.data['expectedRole'] as string[];
    return this.store.select('auth').pipe(
      take(1),
      map((authState) => {
        return authState.user;
      }),
      map((user) => {
        if (user?.role) {
          if (this.user.includes(user?.role)) {
            return true;
          }
        }
        const errorMessage = "You don't have permission to access this page.";
        return this.router.createUrlTree(['/error'], {
          queryParams: { error: errorMessage },
        });
      })
    );
  }
}
