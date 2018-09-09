import { Component, ChangeDetectorRef, ChangeDetectionStrategy, OnInit } from '@angular/core';
import { HttpService } from '../services/httpservice';

@Component({
  selector: 'search-screen-component',
  templateUrl: './searchscreen.component.html',
  styleUrls: ['./searchscreen.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class SearchScreenComponent implements OnInit {
  searchText: string = "";
  charities: any[];
  filteredCharities: any[];
  
  constructor(private cdr: ChangeDetectorRef, private httpService: HttpService) {
  }

  ngOnInit(): void {
    this.httpService.getCharities().then(
      (response) => {
        this.charities = response.charities;
        this.updateSearch(this.searchText);
        this.cdr.markForCheck();
      }
    );
  }

  openMoreDetails(charity: any) {
    
  }

  updateSearch(searchText: string) {
    this.searchText = searchText;
    this.filteredCharities = [];
    for (let charity of this.charities) {
      let name: string = charity.charity_name;
      if (name.toLowerCase().search(this.searchText.toLowerCase()) != -1) {
        this.filteredCharities.push(charity);
      }
    }
    this.cdr.detectChanges();
  }

  getStars(star: number): number[] {
    let stars = [];
    for (let i = 0; i < star; i++) {
      stars.push(i);
    }
    return stars;
  }
}
