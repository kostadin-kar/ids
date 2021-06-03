import { NbMenuService } from '@nebular/theme';
import { Component } from '@angular/core';

@Component({
  selector: 'ngx-welcome',
  styleUrls: ['./welcome.component.scss'],
  templateUrl: './welcome.component.html',
})
export class WelcomeComponent {

  constructor(private menuService: NbMenuService) {
  }

  goToHome() {
    this.menuService.navigateHome();
  }
}
