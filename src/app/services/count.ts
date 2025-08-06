import { Injectable } from '@angular/core';
import { environment } from '../environments/environment';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { catchError, map, Observable, of, timeout } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class Count {
  public count$: Observable<number>;
  constructor( http: HttpClient){
    this.count$ = http.get<{count:number}>(environment.apiUrl).pipe(timeout(5000), map(config=> config.count),
    catchError((error:any)=>{if (error.name==="TimeoutError") {return of(-10)} else {return of(-100)}}));
  }
}
