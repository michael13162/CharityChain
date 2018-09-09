import { Injectable } from "@angular/core";

@Injectable()
export class NavigationService {
    private currentScreen: AppScreen;
    private navigateCallback: () => void;

    constructor() {
        this.currentScreen = AppScreen.Home;
    }

    public getCurrentScreen(): AppScreen {
        return this.currentScreen;
    }

    public navigateTo(screen: AppScreen) {
        this.currentScreen = screen;
        if (this.navigateCallback) {
            this.navigateCallback();
        }
    }

    public setNavigateCallback(callback: () => void) {
        this.navigateCallback = callback;
    }
}

export enum AppScreen {
    Home, Login, CreateAccount, Search, Profile
}