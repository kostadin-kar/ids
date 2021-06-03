import { HttpClient } from '@angular/common/http';
import { Component, OnDestroy } from '@angular/core';
import { Observable, Subscription } from 'rxjs/Rx';

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
    this.subscription = Observable.interval(5000).subscribe(__ => {
      const response = this.http.get('127.0.0.1:5000/view');
      this.responses.push(response);
      this.responses = this.responses.slice(-3);
    }, error => console.log(error))
  }

  stopReceivingAlerts() {
    if (this.subscription) {
      this.subscription.unsubscribe();
    }
  }
}
