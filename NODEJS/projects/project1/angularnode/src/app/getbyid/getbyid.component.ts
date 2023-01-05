import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AppServiceService } from '../app-service.service';

@Component({
  selector: 'app-getbyid',
  templateUrl: './getbyid.component.html',
  styleUrls: ['./getbyid.component.css']
})
export class GetbyidComponent implements OnInit {
  data2:any =[];
  id:any
  result:any
  constructor(private service:AppServiceService,private router:Router) {

  }

  ngOnInit() {
    
   this.getDataidFromAPI();
    // this.postDataFromAPI();
  }
  
  
  getDataidFromAPI(){
    const input = document.getElementById('jjj') as HTMLInputElement;
    const value = input.value;
    console.log(value)
    this.service.getDataid(value).subscribe((res) => {

      console.log('response Id is Id ', )
      // this.result =JSON.stringify(res);
      // this.data2 = res;
      this.data2.push(res);
      console.log(this.data2)

    });
  }
  return(){
    this.router.navigate(['/'])
  }

}
