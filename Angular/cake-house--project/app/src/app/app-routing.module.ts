import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { AuthComponent } from './auth/auth.component';
import { ProductsComponent } from './products/products.component';
import { ProductCreateComponent } from './products/product-create/product-create.component';
import { ProductDetailsComponent } from './products/product-details/product-details.component';
import { ProductsResolverService } from './products/products-resolver.service';
import { AuthGuard } from './auth/auth.guard';
import { ErrorComponent } from './error/error.component';
import { AboutComponent } from './about/about.component';
import { ShoppingComponent } from './shopping/shopping.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'auth', component: AuthComponent },
  {
    path: 'products',

    children: [
      {
        path: '',
        component: ProductsComponent,
        resolve: [ProductsResolverService],
      },
      {
        path: 'new',
        component: ProductCreateComponent,
        canActivate: [AuthGuard],
        data: { expectedRole: ['owner', 'admin'] },
      },
      {
        path: ':slug',
        component: ProductDetailsComponent,
        canActivate: [AuthGuard],
        data: { expectedRole: ['owner', 'admin', 'user'] },
        resolve: [ProductsResolverService],
      },
      {
        path: ':slug/edit',
        component: ProductCreateComponent,
        canActivate: [AuthGuard],
        data: { expectedRole: ['owner', 'admin'] },
        resolve: [ProductsResolverService],
      },
    ],
  },
  {path: 'shopping', component: ShoppingComponent},
  { path: 'about', component: AboutComponent },
  { path: 'error', component: ErrorComponent },
  { path: '**', component: ErrorComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
