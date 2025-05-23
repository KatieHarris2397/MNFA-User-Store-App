import { Component } from '@angular/core';
import { ApiService } from './services/api.service';

@Component({
  selector: 'app-root',
  template: `
    <h1>User Management</h1>
    <form (submit)="createUser($event)">
      <input [(ngModel)]="user.name" name="name" placeholder="Name" required />
      <input [(ngModel)]="user.email" name="email" placeholder="Email" required />
      <button type="submit">Create User</button>
      <button (click)="getUser($event)">Get User</button>
    </form>
    <pre>{{ userDetails | json }}</pre>
  `,
})
export class AppComponent {
  user = { name: '', email: '' };
  userDetails: any;

  constructor(private apiService: ApiService) { }

  createUser(event: Event) {
    event.preventDefault();
    this.apiService.createUser(this.user).subscribe((response) => console.log(response));
  }

  getUser(event: Event) {
    event.preventDefault();
    this.apiService.getUser(this.user.email || '').subscribe((response) => {
      this.userDetails = response;
    });
  }
}
