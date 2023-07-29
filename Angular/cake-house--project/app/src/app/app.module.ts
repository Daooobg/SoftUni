import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { HomeComponent } from './home/home.component';
import { HomeAboutComponent } from './home/home-about/home-about.component';
import { HomeHeroComponent } from './home/home-hero/home-hero.component';
import { HomeAllergenComponent } from './home/home-allergen/home-allergen.component';
import { AuthComponent } from './auth/auth.component';
import { StoreModule } from '@ngrx/store';
import { EffectsModule } from '@ngrx/effects';
import * as fromAuth from './auth/store/auth.reducer';
import { ProductsEffects } from './products/store/products.effects';

import { AuthEffects } from './auth/store/auth.effects';
import { HttpClientModule } from '@angular/common/http';
import { LoadingSpinnerComponent } from './util/loading-spinner/loading-spinner.component';
import { ProductsComponent } from './products/products.component';
import { ProductsListComponent } from './products/products-list/products-list.component';
import { ProductsModule } from './products/products.model';
import { ShortenPipe } from './util/pipes/shorten.pipe';
import { ProductCreateComponent } from './products/product-create/product-create.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    HomeComponent,
    HomeAboutComponent,
    HomeHeroComponent,
    HomeAllergenComponent,
    AuthComponent,
    LoadingSpinnerComponent,
    ProductsComponent,
    ProductsListComponent,
    ShortenPipe,
    ProductCreateComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    StoreModule.forRoot({ auth: fromAuth.authReducer }),
    EffectsModule.forRoot([AuthEffects, ProductsEffects]),
    ProductsModule
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
