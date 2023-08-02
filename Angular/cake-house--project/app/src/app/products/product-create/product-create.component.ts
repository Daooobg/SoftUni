import { Component, OnDestroy, OnInit } from '@angular/core';
import { FormArray, FormControl, FormGroup, Validators } from '@angular/forms';
import { Subscription } from 'rxjs';
import { Store } from '@ngrx/store';

import * as fromApp from '../../store/app.reducer';
import * as productsActions from '../store/products.actions';
import { Product } from '../product.model';
import { ActivatedRoute, Params } from '@angular/router';
@Component({
  selector: 'app-product-create',
  templateUrl: './product-create.component.html',
  styleUrls: ['./product-create.component.css'],
})
export class ProductCreateComponent implements OnInit, OnDestroy {
  isLoading: boolean = false;
  error: string | null = null;
  editMode = false;
  slug: string | null;
  editProduct: Product[] | undefined;

  productForm!: FormGroup;
  productSub: Subscription;

  get imagePathControls() {
    // a getter!
    return (<FormArray>this.productForm.get('imagePath')).controls;
  }

  constructor(
    private store: Store<fromApp.AppStore>,
    private route: ActivatedRoute
  ) {}

  ngOnInit(): void {
    this.route.params.subscribe((params: Params) => {
      this.editMode = params['slug'] != null;
      this.slug = params['slug'];
    });
    this.productSub = this.store.select('products').subscribe((data) => {
      this.isLoading = data.loading;
      this.error = data.productError;
      if (this.editMode) {
        this.editProduct = data.products?.filter(
          (product) => product.slug === this.slug
        );
      }
    });
    this.initForm();
  }

  private initForm() {
    let productName = '';
    let mainImagePath = '';
    let productImagePath = new FormArray<any>([]);
    let productDescription = '';
    let checkboxIngredients = new FormGroup({
      fruit: new FormControl(),
      vegetable: new FormControl(),
      mixed: new FormControl(),
      chocolate: new FormControl(),
      'dairy-free': new FormControl(),
      keto: new FormControl(),
      'nut-free': new FormControl(),
      probiotic: new FormControl(),
      kids: new FormControl(),
    });
    let checkboxSize = new FormGroup({
      '8 Pieces': new FormControl(),
      '10 Pieces': new FormControl(),
      '12 Pieces': new FormControl(),
      '14 Pieces': new FormControl(),
      '16 Pieces': new FormControl(),
    });
    let price = 0;
    if (this.editMode) {
      if (this.editProduct) {
        const product = this.editProduct[0];
        productName = product.name;
        mainImagePath = product.images[0];
        if (product.images.length > 1) {
          for (let i = 1; i < product.images.length; i++) {
            productImagePath.push(
              new FormGroup({
                name: new FormControl(product.images[i]),
              })
            );
          }
        }
        if (product.types) {
          for (let type of product.types) {
            if (type in checkboxIngredients.controls) {
              checkboxIngredients.get(type)?.setValue(true);
            }
          }
        }
        price = product.price;
        if (product.sizes) {
          for (let size of product.sizes) {
            if (size in checkboxSize.controls) {
              checkboxSize.get(size)?.setValue(true);
            }
          }
        }
        productDescription = product.description;
      }
    }
    this.productForm = new FormGroup({
      name: new FormControl(productName, [
        Validators.required,
        Validators.minLength(3),
      ]),
      mainImagePath: new FormControl(mainImagePath, [
        Validators.required,
        Validators.pattern(/^(https?:\/)?\/.*/i),
      ]),
      imagePath: productImagePath,
      description: new FormControl(productDescription, [
        Validators.required,
        Validators.minLength(15),
      ]),
      checkboxIngredients: checkboxIngredients,
      checkboxSize: checkboxSize,
      price: new FormControl(price, Validators.min(0.0001)),
    });
  }

  onAddImagePath() {
    (<FormArray>this.productForm.get('imagePath')).push(
      new FormGroup({
        name: new FormControl(null, [
          Validators.required,
          Validators.pattern(/^(https?:\/)?\/.*/i),
        ]),
      })
    );
  }

  onDeleteImagePath(index: number) {
    (<FormArray>this.productForm.get('imagePath')).removeAt(index);
  }

  getAllImagePaths() {
    let allImages: string[] = [];
    if (this.productForm.get('mainImagePath')?.value != null) {
      allImages.push(this.productForm.get('mainImagePath')?.value);
    }
    if (this.productForm.get('imagePath')?.value) {
      for (let imagePath of this.productForm.get('imagePath')?.value) {
        if (imagePath.name != null) {
          allImages.push(imagePath.name);
        }
      }
    }
    return allImages;
  }

  getCheckboxData(checkbox: string) {
    let checkboxArr: string[] = [];
    const checkboxArrForm = this.productForm.get(checkbox)?.value;
    for (let check in checkboxArrForm) {
      if (checkboxArrForm[check] === true) {
        checkboxArr.push(check);
      }
    }
    return checkboxArr;
  }

  onSubmit() {
    const token: string | null = JSON.parse(
      localStorage.getItem('userData')!
    ).AccessToken;
    const product: Product = {
      description: this.productForm.get('description')?.value,
      images: this.getAllImagePaths(),
      price: this.productForm.get('price')?.value,
      types: this.getCheckboxData('checkboxIngredients'),
      name: this.productForm.get('name')?.value,
      sizes: this.getCheckboxData('checkboxSize'),
    };
    if (this.editMode) {
      console.log(product);
    } else {
      this.store.dispatch(productsActions.creatingStart({ product, token }));
    }
  }

  ngOnDestroy(): void {
    this.productSub.unsubscribe();
  }
}
