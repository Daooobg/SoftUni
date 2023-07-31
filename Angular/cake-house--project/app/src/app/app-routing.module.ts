import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { AuthComponent } from './auth/auth.component';
import { ProductsComponent } from './products/products.component';
import { ProductCreateComponent } from './products/product-create/product-create.component';
import { ProductDetailsComponent } from './products/product-details/product-details.component';
import { ProductsResolverService } from './products/products-resolver.service';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'auth', component: AuthComponent },
  {
    path: 'products',

    children: [
      { path: '', component: ProductsComponent },
      { path: 'new', component: ProductCreateComponent },
      { path: ':slug', component: ProductDetailsComponent, resolve: [ProductsResolverService] },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
