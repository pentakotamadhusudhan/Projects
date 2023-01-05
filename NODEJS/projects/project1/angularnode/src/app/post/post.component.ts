import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AppServiceService } from '../app-service.service';

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.css']
})
export class PostComponent implements OnInit {
  name:any;
  data:any;
  result:any;
  dddaaa:any;

  constructor(private appservice:AppServiceService , private router:Router) {

  }

  ngOnInit(): void {
  
  }
  postDataFromAPI(result: any) {
    this.data = result
    this.appservice.postData(result).subscribe((result) => {
      console.log(this.data);
      this.dddaaa =   JSON.stringify(this.data)

    })

  }
  get(){
    this.router.navigate(['/get'])
  }
  return(){
    this.router.navigate(['/'])
  }
}