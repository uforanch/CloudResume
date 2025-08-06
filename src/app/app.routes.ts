import { Routes } from '@angular/router';
import {Experience } from './components/experience/experience'
import {Portfolio } from './components/portfolio/portfolio'
import { Education } from './components/education/education';
import { Welcome } from './components/welcome/welcome';
export const routes: Routes = [
    {path:"welcome", component:Welcome},
    {path:"education", component:Education},
    {path:"experience", component:Experience},
    {path:"portfolio", component:Portfolio},
    {path:"", redirectTo:"/welcome", pathMatch:"full"}
];
