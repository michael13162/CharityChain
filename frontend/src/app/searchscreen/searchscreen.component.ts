import { Component, ChangeDetectionStrategy, OnInit } from '@angular/core';
import { HttpService } from '../services/httpservice';

@Component({
  selector: 'search-screen-component',
  templateUrl: './searchscreen.component.html',
  styleUrls: ['./searchscreen.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class SearchScreenComponent implements OnInit {
  searchText: string;
  charities: any[];
  
  constructor(private httpService: HttpService) {
  }

  ngOnInit(): void {
    this.httpService.getCharities().then(
      (response) => {this.charities = response.charities}
    );
  }
}
