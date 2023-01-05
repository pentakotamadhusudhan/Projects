import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { GetComponent } from './get/get.component';
import { GetbyidComponent } from './getbyid/getbyid.component';
import { LoginComponent } from './login/login.component';

import { MainComponent } from './main/main.component';
import { PostComponent } from './post/post.component';

const routes: Routes = [
  {path: 'get', component: GetComponent},
  {path: 'getid/:id', component: GetbyidComponent},
  {path: 'post',component: PostComponent},
  {path: '', component: MainComponent},
  {path: 'login', component:LoginComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
