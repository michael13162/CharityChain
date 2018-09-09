import { Component, ChangeDetectionStrategy, OnInit, ChangeDetectorRef } from '@angular/core';
import { NavigationService } from '../services/navigationservice';
import { HttpService } from '../services/httpservice';
import { UserService } from '../services/userservice';

@Component({
  selector: 'profile-screen-component',
  templateUrl: './profilescreen.component.html',
  styleUrls: ['./profilescreen.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ProfileScreenComponent implements OnInit {
  jsonProfile: any;

  constructor(private cdr: ChangeDetectorRef, private navigationService: NavigationService, private httpService: HttpService, private userService: UserService) {
  }

  public isCharity() {
    return this.userService.isCharity();
  }

  ngOnInit(): void {
    this.httpService.getCharityInformation(this.userService.getEin()).then(
      (value) => {
        this.jsonProfile = value;
        this.cdr.markForCheck();
      }
    );
  }
}
