import { Injectable } from "@angular/core";

@Injectable()
export class NavigationService {
    private currentScreen: AppScreen;
    constructor() {
        this.currentScreen = AppScreen.Home;
    }

    public getCurrentScreen(): AppScreen {
        return this.currentScreen;
    }

    public navigateTo(screen: AppScreen) {
        this.currentScreen = screen;
    }
}

export enum AppScreen {
    Home, Login, CreateAccount, Search, Profile
}