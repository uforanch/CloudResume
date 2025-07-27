import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { Count } from '../../services/count';
@Component({
  selector: 'app-navbar',
  imports: [RouterModule],
  templateUrl: './navbar.html',
  styleUrl: './navbar.css'
})
export class Navbar {
  constructor(getCount: Count){}


}
