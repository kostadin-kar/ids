import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Component, OnDestroy, OnInit } from '@angular/core';
import { LocalDataSource } from 'ng2-smart-table';
import { Subscription, throwError } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';

@Component({
  selector: 'ngx-smart-table',
  templateUrl: './story.component.html',
  styleUrls: ['./story.component.scss'],
})
export class StoryComponent implements OnDestroy, OnInit {

  settings = {
    actions: {
      edit: false
    },
    add: {
      addButtonContent: '<i class="nb-plus"></i>',
      createButtonContent: '<i class="nb-checkmark"></i>',
      cancelButtonContent: '<i class="nb-close"></i>',
      confirmCreate: true
    },
    delete: {
      deleteButtonContent: '<i class="nb-trash"></i>',
      confirmDelete: true,
    },
    columns: {
      author: {
        title: 'Author',
        type: 'string',
      },
      description: {
        title: 'Description',
        type: 'string',
      },
      headline: {
        title: 'Headline',
        type: 'string',
      },
      id: {
        title: 'ID',
        type: 'number',
      },
      published: {
        title: 'Published on',
        type: 'string',
      },
      rating: {
        title: 'Rating',
        type: 'number',
      },
      story: {
        title: 'Story',
        type: 'string',
      }
    },
  };

  source: LocalDataSource = new LocalDataSource();
  subscription: Subscription;

  constructor(private http: HttpClient) {
  }

  ngOnInit() {
    this.subscription = this.http.get<string>('http://127.0.0.1:5001/stories')
    .subscribe(jsonArr => {
      const stories: any = jsonArr;
      this.source.load(stories);
    }, error => console.log(error));
  }

  ngOnDestroy() {
    if(this.subscription) {
      this.subscription.unsubscribe();
    }
  }

  onDeleteConfirm(event): void {
    if (window.confirm('Are you sure you want to delete?')) {
      this.http.delete(`http://127.0.0.1:5001/stories/${event.data.id}`)
        .pipe(catchError(this.handleError))
        .subscribe()

      this.source.remove(event.data)
      
      event.confirm.resolve();
    } else {
      event.confirm.reject();
    }
  }

  onCreateConfirm(event): void {
    this.http.post(`http://127.0.0.1:5001/stories`, event.newData)
      .pipe(tap(_ => console.log('Added new story')), catchError(this.handleError))
      .subscribe();
    
    event.confirm.resolve();
  }

  private handleError(error: HttpErrorResponse) {
    if (error.status === 0) {
      console.error('An error occurred:', error.error);
    } else {
      console.error(
        `Backend returned code ${error.status}, ` +
        `body was: ${error.error}`);
    }
    return throwError(
      'Something bad happened; please try again later.');
  }
}
