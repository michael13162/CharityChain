import { Injectable } from "@angular/core";

@Injectable()
export class UserService {
    private signedIn: boolean = false;
    private username: string;
    private password: string;
    private charity: boolean;
    private ein: string;
    private balance: number;

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
    }

    isSignedIn(): boolean {
        return this.signedIn;
    }

    isCharity(): boolean {
        return this.charity;
    }

    signOut() {
        this.signedIn = false;
        this.username = undefined;
        this.password = undefined;
        this.charity = undefined;
        this.ein = undefined;
        this.balance = undefined;
    }
}