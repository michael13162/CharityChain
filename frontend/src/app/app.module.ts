import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { HomeScreenComponent } from './homescreen/homescreen.component';
import { NavigationService } from './services/navigationservice';
import { UserService } from './services/userservice';
import { HttpService } from './services/httpservice';
import { LoginScreenComponent } from './loginscreen/loginscreen.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    HomeScreenComponent,
    LoginScreenComponent,
  ],
  imports: [
    BrowserModule
  ],
  providers: [HttpService, NavigationService, UserService],
  bootstrap: [AppComponent]
})
export class AppModule { }
