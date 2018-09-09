import { Component, ChangeDetectionStrategy } from '@angular/core';
import { NavigationService, AppScreen } from '../services/navigationservice';

@Component({
  selector: 'header-component',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class HeaderComponent {
    AppScreen = AppScreen;

    constructor(private navigationService: NavigationService) {
    }

    switchScreen(screen: AppScreen) {
      this.navigationService.navigateTo(screen);
    }
}
