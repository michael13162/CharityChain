import { Injectable } from "@angular/core";
import { HttpClient } from '@angular/common/http';
import { UserService } from "./userservice";

@Injectable()
export class HttpService {
    baseUrl: string = "http://localhost:1234/";

    constructor(private httpClient: HttpClient, private userService: UserService) {}

    login(username: string, password: string): Promise<any> {
        const endpoint = this.baseUrl + "login";
        return this.httpClient.post(endpoint, {username: username, password: password}).toPromise();
    }

    register(username: string, password: string, charity: boolean, ein: string): Promise<any> {
        const endpoint = this.baseUrl + "register";
        return this.httpClient.post(endpoint, {username: username, password: password, is_charity: charity ? 1 : 0, ein: ein}).toPromise().then(
            (value) => {this.userService.signIn(value);}
        );
    }
}