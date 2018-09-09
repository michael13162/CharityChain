import { Component, ChangeDetectionStrategy } from '@angular/core';
import { NavigationService, AppScreen } from './services/navigationservice';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class AppComponent {
  AppScreen = AppScreen;

  constructor(private navigationService: NavigationService) {
  }

  public get currentScreen(): AppScreen {
    return this.navigationService.getCurrentScreen();
  }
}
