import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { NotFoundComponent } from '../miscellaneous/not-found/not-found.component';
import { AlertComponent } from './ids/alert.component';
import { IntruderComponent } from './intruder/intruder.component';

import { LayoutComponent } from './layout.component';
import { StoryComponent } from './story/story.component';

const routes: Routes = [{
  path: '',
  component: LayoutComponent,
  children: [
    {
      path: 'intruder',
      component: IntruderComponent,
    },
    {
      path: 'ids',
      component: AlertComponent,
    },
    {
      path: 'story',
      component: StoryComponent
    },
    {
      path: '**',
      component: NotFoundComponent,
    },
  ],
}];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class LayoutRoutingModule {
}
