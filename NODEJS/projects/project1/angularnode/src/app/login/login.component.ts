import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AppServiceService } from '../app-service.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  results: any;
  constructor(private appservice: AppServiceService, private router: Router) { }

  ngOnInit(): void {
  }
  loginDataFromAPI(data:any){
    this.appservice.loginData(data).subscribe({next:results=>{
      console.log(results)
      // this.router.navigate(['/get'])
      this.results=JSON.stringify(results)
    }});
  }
  return(){
    this.router.navigate(['/'])
  }

}
