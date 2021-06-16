import { Component } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { catchError, tap } from 'rxjs/operators';
import { throwError } from 'rxjs/internal/observable/throwError';

@Component({
  selector: 'ngx-intruder',
  styleUrls: ['./intruder.component.scss'],
  templateUrl: './intruder.component.html',
})
export class IntruderComponent {

  constructor(private http: HttpClient) {}

  startAttack() {
    return this.http.post('http://127.0.0.1:5002/dashboard?action=start', null)
      .pipe(
        tap(_ => console.log('attack started')),
        catchError(this.handleError)
      )
      .subscribe()
  }

  stopAttack() {
    return this.http.post('http://127.0.0.1:5002/dashboard?action=stop', null)
      .pipe(
        tap(_ => console.log('attack stopped')),
        catchError(this.handleError)
      )
      .subscribe()
  }

  private handleError(error: HttpErrorResponse) {
    if (error.status === 0) {
      // A client-side or network error occurred. Handle it accordingly.
      console.error('An error occurred:', error.error);
    } else {
      // The backend returned an unsuccessful response code.
      // The response body may contain clues as to what went wrong.
      console.error(
        `Backend returned code ${error.status}, ` +
        `body was: ${error.error}`);
    }
    // Return an observable with a user-facing error message.
    return throwError(
      'Something bad happened; please try again later.');
  }
}
