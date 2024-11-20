import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ApiService {

  constructor(private http: HttpClient) {}

  createUser(user: any): Observable<any> {
    return this.http.post(`/api/user/`, user);
  }

  getUser(userId: string): Observable<any> {
    return this.http.get(`/api/user/${userId}`);
  }
}
