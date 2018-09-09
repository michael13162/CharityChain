import { Component, ChangeDetectionStrategy, ChangeDetectorRef } from '@angular/core';
import { NavigationService, AppScreen } from '../services/navigationservice';
import { HttpService } from '../services/httpservice';

@Component({
  selector: 'create-account-component',
  templateUrl: './createaccount.component.html',
  styleUrls: ['./createaccount.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class CreateAccountComponent {
  username: string;
  password: string;
  confirmPassword: string;
  charity: boolean;
  passwordsDontMatch: boolean = false;
  timeElapsed: boolean = false;
  ein: string;

  constructor(private cdr: ChangeDetectorRef, private navigationService: NavigationService, private httpService: HttpService) {
  }

  switchToLogin() {
    this.navigationService.navigateTo(AppScreen.Login);
  }

  register() {
    if (this.password === this.confirmPassword) {
      this.httpService.register(this.username, this.password, true, this.charity ? this.ein : "").then(() => {this.navigationService.navigateTo(AppScreen.Search)});
    } else {
      this.passwordsDontMatch = true;
      this.timeElapsed = false;
      setTimeout(() => {
        this.passwordsDontMatch = false;
        this.timeElapsed = true;
        this.cdr.markForCheck();
      }, 2000);
    }
  }
}
