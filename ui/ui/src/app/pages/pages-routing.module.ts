import { RouterModule, Routes } from '@angular/router';
import { NgModule } from '@angular/core';

import { PagesComponent } from './pages.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { StoryComponent } from './story/story.component';
import { IdsComponent } from './ids/ids.component';
import { IntruderComponent } from './intruder/intruder.component';

const routes: Routes = [{
  path: '',
  component: PagesComponent,
  children: [
    {
      path: 'service',
      component: StoryComponent,
    },
    {
      path: 'ids',
      component: IdsComponent,
    },
    {
      path: 'intruder',
      component: IntruderComponent,
    },
    {
      path: '',
      redirectTo: 'service',
      pathMatch: 'full',
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
export class PagesRoutingModule {
}
