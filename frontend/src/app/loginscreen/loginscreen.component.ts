import { Component, ChangeDetectionStrategy } from '@angular/core';
import { NavigationService, AppScreen } from '../services/navigationservice';
import { HttpService } from '../services/httpservice';

@Component({
  selector: 'login-screen-component',
  templateUrl: './loginscreen.component.html',
  styleUrls: ['./loginscreen.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class LoginScreenComponent {
    username: string;
    password: string;

    constructor(private navigationService: NavigationService, private httpService: HttpService) {
    }
    
    switchToCreateAccount() {
        this.navigationService.navigateTo(AppScreen.CreateAccount);
    }

    login() {
        this.httpService.login(this.username, this.password).then(() => {
            this.navigationService.navigateTo(AppScreen.Search);
        });
    }
}
