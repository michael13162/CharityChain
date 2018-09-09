import { Component, ChangeDetectionStrategy, ChangeDetectorRef } from '@angular/core';
import { NavigationService, AppScreen } from './services/navigationservice';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class AppComponent {
  AppScreen = AppScreen;

  constructor(private cdr: ChangeDetectorRef, private navigationService: NavigationService) {
    this.navigationService.setNavigateCallback(() => {
      this.cdr.markForCheck();
    });
  }

  public get currentScreen(): AppScreen {
    return this.navigationService.getCurrentScreen();
  }
}
