import { Routes } from '@angular/router';
import {Socials } from './components/socials/socials'
import {Experience } from './components/experience/experience'
import {Portfolio } from './components/portfolio/portfolio'
export const routes: Routes = [
    {path:"socials", component:Socials},
    {path:"experience", component:Experience},
    {path:"portfolio", component:Portfolio},
    {path:"", redirectTo:"/socials", pathMatch:"full"}
];
