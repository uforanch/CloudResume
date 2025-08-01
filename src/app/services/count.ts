import { Injectable } from '@angular/core';
import { environment } from '../environments/environment';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class Count {
  private count = 0;
  constructor( http: HttpClient){
    http.get(environment.apiUrl).subscribe(config=>{console.log(config); this.count = (config as {count:number}).count})
  }
  getCount(): number {return this.count;}
}
