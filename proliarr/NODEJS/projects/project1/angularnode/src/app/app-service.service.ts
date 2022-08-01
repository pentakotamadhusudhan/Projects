import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';  

@Injectable({
  providedIn: 'root'
})
export class AppServiceService {

  constructor(private http: HttpClient) { }
  getData(){
    return this.http.get('api/get')
  }
  getDataid(id:any){
    console.log()
    return this.http.get('api/getid/'+id)
  }

  postData(data:any){
    // console.log(data)
    return this.http.post('api/post',data)
  }
  loginData(data:any){
    // console.log(data)
    return this.http.post('api/login',data)
  }


}
