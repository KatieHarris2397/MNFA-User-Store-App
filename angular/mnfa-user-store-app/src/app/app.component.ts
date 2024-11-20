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
    </form>
    <button (click)="getUser()">Get User</button>
    <pre>{{ userDetails | json }}</pre>
  `,
})
export class AppComponent {
  user = { name: '', email: '' };
  userDetails: any;

  constructor(private apiService: ApiService) { }

  createUser(event: Event) {
    event.preventDefault();
    this.apiService.createUser(this.user).subscribe((res) => console.log(res));
  }

  getUser() {
    const userId = prompt('Enter User ID');
    this.apiService.getUser(userId || '').subscribe((res) => {
      this.userDetails = res;
    });
  }
}
