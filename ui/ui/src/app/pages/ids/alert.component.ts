import { HttpClient } from '@angular/common/http';
import { Component, OnDestroy } from '@angular/core';
import { interval, Subscription } from 'rxjs';
import { tap } from 'rxjs/operators';

@Component({
  selector: 'ngx-alert',
  templateUrl: 'alert.component.html',
})
export class AlertComponent implements OnDestroy {
  responses = [];
  subscription: Subscription;
  
  constructor(private http: HttpClient) {}

  ngOnDestroy() {
    this.stopReceivingAlerts();
  }

  startReceivingAlerts() {
    if (this.subscription) {
      return;
    }

    console.log('starting')
    this.subscription = interval(3000).pipe(
      tap(_ => {
        console.log("trying")
        const response = this.http.get('http://127.0.0.1:5000/state')
          .subscribe(alert => {
            const res: any = alert;
            const status = res.global_state[0];
            console.log(alert)
            this.responses.push(status);
            this.responses = this.responses.slice(-3);

            if (response) {
              response.unsubscribe();
            }
          }, error => console.log(error));
      })
    ).subscribe();
  }

  stopReceivingAlerts() {
    console.log('stopping')

    if (this.subscription) {
      this.subscription.unsubscribe();
    }
  }
}
