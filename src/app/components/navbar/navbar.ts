import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { Count } from '../../services/count';
import { AsyncPipe } from '@angular/common';
import { Observable } from 'rxjs';
@Component({
  selector: 'app-navbar',
  imports: [RouterModule, AsyncPipe],
  templateUrl: './navbar.html',
  styleUrl: './navbar.css'
})
export class Navbar {
  private countService: Count;
  public count$: Observable<number>;
  constructor(countService: Count){
    this.countService = countService;
    this.count$ = this.countService.count$;
  }

}
