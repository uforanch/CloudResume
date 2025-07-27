import { Routes } from '@angular/router';
import {Experience } from './components/experience/experience'
import {Portfolio } from './components/portfolio/portfolio'
import { Education } from './components/education/education';
export const routes: Routes = [
    {path:"education", component:Education},
    {path:"experience", component:Experience},
    {path:"portfolio", component:Portfolio},
    {path:"", redirectTo:"/education", pathMatch:"full"}
];
