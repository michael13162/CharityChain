import { Component, ChangeDetectionStrategy } from '@angular/core';

@Component({
  selector: 'search-screen-component',
  templateUrl: './searchscreen.component.html',
  styleUrls: ['./searchscreen.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class SearchScreenComponent {
    searchText: string;
    
    constructor() {
    }
}
