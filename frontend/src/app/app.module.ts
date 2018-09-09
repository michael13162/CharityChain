import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule }   from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { HomeScreenComponent } from './homescreen/homescreen.component';
import { NavigationService } from './services/navigationservice';
import { UserService } from './services/userservice';
import { HttpService } from './services/httpservice';
import { LoginScreenComponent } from './loginscreen/loginscreen.component';
import { CreateAccountComponent } from './createaccountscreen/createaccount.component';
import { SearchScreenComponent } from './searchscreen/searchscreen.component';
import { ProfileScreenComponent } from './profilescreen/profilescreen.component';
import { ProfileWellComponent } from './profilewell/profilewell.component';

@NgModule({
  declarations: [
    AppComponent,
    CreateAccountComponent,
    HeaderComponent,
    HomeScreenComponent,
    LoginScreenComponent,
    ProfileScreenComponent,
    ProfileWellComponent,
    SearchScreenComponent,
  ],
  imports: [
    BrowserModule,
    CommonModule,
    FormsModule,
    HttpClientModule,
  ],
  providers: [HttpService, NavigationService, UserService],
  bootstrap: [AppComponent]
})
export class AppModule { }
