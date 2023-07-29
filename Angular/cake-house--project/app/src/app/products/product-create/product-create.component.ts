import { Component, OnInit } from '@angular/core';
import { FormArray, FormControl, FormGroup, Validators } from '@angular/forms';
@Component({
  selector: 'app-product-create',
  templateUrl: './product-create.component.html',
  styleUrls: ['./product-create.component.css'],
})
export class ProductCreateComponent implements OnInit {
  productForm: FormGroup;

  get imagePathControls() {
    // a getter!
    return (<FormArray>this.productForm.get('imagePath')).controls;
  }

  ngOnInit(): void {
    this.initForm();
  }

  private initForm() {
    let productName = '';
    let mainImagePath = '';
    let productImagePath = new FormArray([]);
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
      '4 Pieces': new FormControl(),
      '6 Pieces': new FormControl(),
      '8 Pieces': new FormControl(),
      '10 Pieces': new FormControl(),
    });
    let price = 0;

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
    console.log(this.productForm.value);
    console.log(this.productForm);
    const allImages = this.getAllImagePaths();
    const checkboxSize = this.getCheckboxData('checkboxSize');
    const checkboxIng = this.getCheckboxData('checkboxIngredients');

    console.log(checkboxIng);
    console.log(checkboxSize);
    console.log(allImages);
  }
}
