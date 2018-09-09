import { Injectable } from "@angular/core";

@Injectable()
export class UserService {
    private signedIn: boolean = false;
    private username: string;
    private password: string;
    private charity: boolean;
    private ein: string;
    private balance: number;

    signInOutCallback: () => void;

    constructor() {}

    signIn(user: any) {
        this.signedIn = true;
        this.username = user.username;
        this.password = user.password;
        this.charity = user.is_charity == 1;
        if (this.charity) {
            this.ein = user.ein;
            this.balance = user.balance;
        }
        if (this.signInOutCallback) {
            this.signInOutCallback();
        }
    }

    signOut() {
        this.signedIn = false;
        this.username = undefined;
        this.password = undefined;
        this.charity = undefined;
        this.ein = undefined;
        this.balance = undefined;
        if (this.signInOutCallback) {
            this.signInOutCallback();
        }
    }

    setSignInOutCallback(callback: () => void) {
        this.signInOutCallback = callback;
    }

    isSignedIn(): boolean {
        return this.signedIn;
    }

    isCharity(): boolean {
        return this.charity;
    }
}