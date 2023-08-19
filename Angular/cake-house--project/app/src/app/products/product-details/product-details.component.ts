import { Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';
import { Store } from '@ngrx/store';
import { NgForm } from '@angular/forms';

import { Product } from '../product.model';
import * as fromApp from '../../store/app.reducer';
import * as productsActions from '../store/products.actions';
import { AuthService } from 'src/app/auth/auth.service';
import { User } from 'src/app/auth/user.model';

interface Comment {
  comment: String;
  rating: Number;
  ownerId: { _id: String; name: String };
}

@Component({
  selector: 'app-product-details',
  templateUrl: './product-details.component.html',
  styleUrls: ['./product-details.component.css'],
})
export class ProductDetailsComponent implements OnInit, OnDestroy {
  token: string | null;
  product: Product | any;
  error: string;
  activeImg: string;
  activeSize: string;
  price: number;
  user: User;
  buttonContent = 'Description';
  selectedOption: string = '5 Stars';
  options: string[] = ['1 Star', '2 Stars', '3 Stars', '4 Stars', '5 Stars'];
  isComment: []

  isLoading: boolean = false;
  errorOnDelete: string | null = null;

  productSub: Subscription;

  constructor(
    private route: ActivatedRoute,
    private store: Store<fromApp.AppStore>,
    private authService: AuthService
  ) {}
  ngOnInit(): void {
    this.route.data.subscribe((data: any) => {
      this.product = data[0].product as Product | null;
    });
    this.setActiveImg(0);
    this.setActiveSize(this.product.sizes[0]);
    if (!this.product) {
      this.error = 'Something went wrong';
    }

    this.productSub = this.store.select('products').subscribe((product) => {
      this.isLoading = product.loading;
      this.errorOnDelete = product.productError;
    });
    this.authService.getUser().subscribe((authData) => {
      if (authData.user?.role) {
        this.user = authData.user;
      }
    });
    this.isComment = this.product.comments.filter((comment: Comment) => comment.ownerId._id === this.user.userId)
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

  onButtonChange(event: Event) {
    const target = event.target as HTMLElement;
    if (target.textContent) {
      this.buttonContent = target.textContent.trim();
    }
  }

  onDelete() {
    this.store.dispatch(
      productsActions.deleteProduct({
        slug: this.product.slug,
        token: this.user.token,
      })
    );
  }

  onSubmitComment(form: NgForm) {
    const token: string | null = JSON.parse(
      localStorage.getItem('userData')!
    ).AccessToken;
    this.store.dispatch(
      productsActions.createComment({
        slug: this.product.slug,
        comment: {
          rating: +form.value.options.split(' ')[0],
          comment: form.value.comment,
        },
        token,
        ownerId: { _id: this.user.userId, name: this.user.username },
      })
    );
  }

  getTempStars() {
    const tempStars = [];
    for (let index = 0; index < 5; index++) {
      const number = index + 0.5;
      if (this.product.averageRating >= index + 1) {
        tempStars.push('star');
      } else if (this.product.averageRating >= number) {
        tempStars.push('star_half');
      } else {
        tempStars.push('star_border');
      }
    }
    return tempStars;
  }
  ngOnDestroy(): void {
    this.productSub.unsubscribe();
  }
}
