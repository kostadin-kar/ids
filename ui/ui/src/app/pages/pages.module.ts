import { CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { NbAccordionModule, NbButtonModule, NbCardModule, NbListModule, NbMenuModule, NbRouteTabsetModule, NbStepperModule, NbTabsetModule, NbUserModule } from '@nebular/theme';

import { ThemeModule } from '../@theme/theme.module';
import { PagesComponent } from './pages.component';
import { PagesRoutingModule } from './pages-routing.module';
import { WelcomeComponent } from './welcome/welcome.component';
import { IntruderComponent } from './intruder/intruder.component';
import { AlertComponent } from './ids/alert.component';
import { StoryComponent } from './story/story.component';
import { NotFoundComponent } from './not-found/not-found.component';

@NgModule({
  imports: [
    PagesRoutingModule,
    ThemeModule,
    NbMenuModule,
    NbTabsetModule,
    NbRouteTabsetModule,
    NbStepperModule,
    NbCardModule,
    NbButtonModule,
    NbListModule,
    NbAccordionModule,
    NbUserModule,
  ],
  declarations: [
    PagesComponent,
    WelcomeComponent,
    IntruderComponent,
    AlertComponent,
    StoryComponent,
    NotFoundComponent,
  ],
  schemas:[CUSTOM_ELEMENTS_SCHEMA]
})
export class PagesModule {
}
