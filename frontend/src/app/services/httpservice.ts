import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { UserService } from "./userservice";

@Injectable()
export class HttpService {
    baseUrl: string = "http://127.0.0.1:5000/";
    private readonly HTTP_OPTIONS = {
        headers: new HttpHeaders({
            'Content-Type':  'application/json',
        })
    };

    constructor(private httpClient: HttpClient, private userService: UserService) {}

    login(username: string, password: string): Promise<any> {
        const endpoint = this.baseUrl + "login";
        return this.httpClient.post(endpoint, {username: username, password: password}, this.HTTP_OPTIONS).toPromise().then(
            (value) => {this.userService.signIn(value);}
        );
    }

    register(username: string, password: string, charity: boolean, ein: string): Promise<any> {
        const endpoint = this.baseUrl + "register";
        return this.httpClient.post(endpoint, {username: username, password: password, is_charity: charity ? 1 : 0, ein: ein}, this.HTTP_OPTIONS).toPromise().then(
            (value) => {this.userService.signIn(value);}
        );
    }

    getCharities(): Promise<any> {
        const endpoint = this.baseUrl + "charities";
        return this.httpClient.get(endpoint, this.HTTP_OPTIONS).toPromise();
    }
}