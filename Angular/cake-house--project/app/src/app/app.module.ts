import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { HomeComponent } from './home/home.component';
import { HomeAboutComponent } from './home/home-about/home-about.component';
import { HomeHeroComponent } from './home/home-hero/home-hero.component';
import { HomeAllergenComponent } from './home/home-allergen/home-allergen.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    HomeComponent,
    HomeAboutComponent,
    HomeHeroComponent,
    HomeAllergenComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
