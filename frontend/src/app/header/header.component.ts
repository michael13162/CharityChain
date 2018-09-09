import { Component, ChangeDetectionStrategy } from '@angular/core';
import { NavigationService, AppScreen } from '../services/navigationservice';
import { UserService } from '../services/userservice';

@Component({
  selector: 'header-component',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class HeaderComponent {
  AppScreen = AppScreen;

  constructor(private navigationService: NavigationService, private userService: UserService) {
  }

  switchScreen(screen: AppScreen) {
    this.navigationService.navigateTo(screen);
  }

  signedIn(): boolean {
    return this.userService.isSignedIn();
  }
  
  isCharity(): boolean {
    return this.signedIn() && this.userService.isCharity();
  }

  signOut() {
    this.userService.signOut();
    this.navigationService.navigateTo(AppScreen.Home);
  }
}
