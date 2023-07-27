import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.css'],
})
export class AuthComponent implements OnInit {
  isVisible = false;
  isLogin = true;

  ngOnInit(): void {
  }

  onChangeVisibility() {
    this.isVisible = !this.isVisible;
  }

  onChangeForm() {
    this.isLogin = !this.isLogin;
  }

  onSubmit(form: NgForm) {
    console.log(form);
    form.reset()
  }
}
