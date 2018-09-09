import { Component, ChangeDetectionStrategy, OnInit, ChangeDetectorRef } from '@angular/core';
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

  constructor(private cdr: ChangeDetectorRef, private httpService: HttpService, private userService: UserService) {
  }

  ngOnInit(): void {
    this.httpService.getCharityInformation(this.userService.getEin()).then(
      (value) => {
        this.jsonProfile = value;
        this.cdr.detectChanges();
      }
    );
  }
}
