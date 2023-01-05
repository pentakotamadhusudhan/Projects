import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AppServiceService } from '../app-service.service';


@Component({
  selector: 'app-get',
  templateUrl: './get.component.html',
  styleUrls: ['./get.component.css']
})
export class GetComponent implements OnInit {
  // data: any;
  data3: any;
  constructor(private service:AppServiceService,private router:Router) {

  }

  ngOnInit(): void {
    this.getDataFromAPI();
  }

  getDataFromAPI() {
    this.service.getData().subscribe((data) => {
      console.log('response is API is ', data)
      // this.data = data;
      this.data3 = data;
      // this.data3.push(data);
      console.log(this.data3)
    },(error)=>{
      console.log('error is ', error);
    }
    )} 
    return(){
      this.router.navigate(['/'])
    }

}
