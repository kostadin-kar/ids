import { HttpClient } from '@angular/common/http';
import { Component, OnDestroy } from '@angular/core';
import { LocalDataSource } from 'ng2-smart-table';
import { Subscription } from 'rxjs';

@Component({
  selector: 'ngx-smart-table',
  templateUrl: './story.component.html',
  styleUrls: ['./story.component.scss'],
})
export class StoryComponent implements OnDestroy {

  settings = {
    add: {
      addButtonContent: '<i class="nb-plus"></i>',
      createButtonContent: '<i class="nb-checkmark"></i>',
      cancelButtonContent: '<i class="nb-close"></i>',
    },
    // edit: {
    //   editButtonContent: '<i class="nb-edit"></i>',
    //   saveButtonContent: '<i class="nb-checkmark"></i>',
    //   cancelButtonContent: '<i class="nb-close"></i>',
    // },
    delete: {
      deleteButtonContent: '<i class="nb-trash"></i>',
      confirmDelete: true,
    },
    columns: {
      id: {
        title: 'ID',
        type: 'number',
      },
      headline: {
        title: 'Headline',
        type: 'string',
      },
      description: {
        title: 'Description',
        type: 'string',
      },
      story: {
        title: 'Story',
        type: 'string',
      },
      author: {
        title: 'Author',
        type: 'string',
      },
      published: {
        title: 'Published on',
        type: 'string',
      },
      rating: {
        title: 'Rating',
        type: 'number',
      }
    },
  };

  source: LocalDataSource = new LocalDataSource();
  subscription: Subscription;

  constructor(private http: HttpClient) {

    this.subscription = this.http.get('127.0.0.1:5001/stories')
      .subscribe(response => {
        const stories: any[] = [response];
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
      event.confirm.resolve();
    } else {
      event.confirm.reject();
    }
  }

  onCreateConfirm(event): void {

  }
}
