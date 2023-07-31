import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { Product } from '../product.model';

@Component({
  selector: 'app-product-details',
  templateUrl: './product-details.component.html',
  styleUrls: ['./product-details.component.css'],
})
export class ProductDetailsComponent implements OnInit {
  product: Product | any;
  error: string;
  activeImg: string;
  activeSize: string;
  price: number;

  constructor(private route: ActivatedRoute) {}
  ngOnInit(): void {
    this.route.data.subscribe((data: any) => {
      this.product = data[0].product as Product | null;
    });
    this.setActiveImg(0);
    this.setActiveSize(this.product.sizes[0]);
    if (!this.product) {
      this.error = 'Something went wrong';
    }
  }

  setActiveImg(i: number) {
    this.activeImg = this.product.images[i];
  }

  setActiveSize(size: string) {
    this.activeSize = size;
    if (this.activeSize) {
      this.price = +this.activeSize.slice(0, 2) * this.product.price;
    }
  }
}
