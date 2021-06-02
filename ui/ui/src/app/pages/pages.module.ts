import { NgModule } from '@angular/core';
import { NbMenuModule } from '@nebular/theme';

import { PagesComponent } from './pages.component';
import { PagesRoutingModule } from './pages-routing.module';
import { StoryModule } from './story/story.module';
import { IdsModule } from './ids/ids.module';
import { IntruderModule } from './intruder/intruder.module';
import { ThemeModule } from './theme/theme.module';

@NgModule({
  imports: [
    PagesRoutingModule,
    ThemeModule,
    NbMenuModule,
    StoryModule,
    IdsModule,
    IntruderModule,
  ],
  declarations: [
    PagesComponent,
  ],
})
export class PagesModule {
}
