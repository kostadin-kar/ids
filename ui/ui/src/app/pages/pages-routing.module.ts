import { RouterModule, Routes } from '@angular/router';
import { NgModule } from '@angular/core';

import { PagesComponent } from './pages.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { IntruderComponent } from './intruder/intruder.component';
import { AlertComponent } from './ids/alert.component';
import { StoryComponent } from './story/story.component';
import { NotFoundComponent } from './not-found/not-found.component';

const routes: Routes = [{
  path: '',
  component: PagesComponent,
  children: [
    {
      path: 'main',
      component: WelcomeComponent
    },
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
      path: '',
      redirectTo: 'main',
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
