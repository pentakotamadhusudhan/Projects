import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AppServiceService } from '../app-service.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  constructor(private appservice: AppServiceService, private router: Router,) { }

  ngOnInit(): void {
  }
  get(){
    this.router.navigate(['/get']);
  }
  getbyid(){
    this.router.navigate(['/getid/:id'])
  }
  post(){
    this.router.navigate(['/post'])
  }
  login(){
    this.router.navigate(['/login'])}
}
