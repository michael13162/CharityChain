import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { HomeScreenComponent } from './homescreen/homescreen.component';
import { NavigationService } from './services/navigationservice';
import { UserService } from './services/userservice';
import { HttpService } from './services/httpservice';
import { LoginScreenComponent } from './loginscreen/loginscreen.component';
import { CreateAccountComponent } from './createaccountscreen/createaccount.component';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    CreateAccountComponent,
    HeaderComponent,
    HomeScreenComponent,
    LoginScreenComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
  ],
  providers: [HttpService, NavigationService, UserService],
  bootstrap: [AppComponent]
})
export class AppModule { }
