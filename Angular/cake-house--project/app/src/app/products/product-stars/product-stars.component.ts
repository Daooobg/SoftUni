import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-product-stars',
  templateUrl: './product-stars.component.html',
  styleUrls: ['./product-stars.component.css'],
})
export class ProductStarsComponent {
  @Input() stars: number = 0;

  getTempStars() {
    const tempStars = [];
    for (let index = 0; index < 5; index++) {
      const number = index + 0.5;
      if (this.stars >= index + 1) {
        tempStars.push('star');
      } else if (this.stars >= number) {
        tempStars.push('star_half');
      } else {
        tempStars.push('star_border');
      }
    }
    return tempStars;
  }
}
