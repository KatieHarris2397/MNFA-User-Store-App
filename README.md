# MNFA-User-Store-App
A simple user storing app to demonstrate a MongoDB-Neo4j-FastAPI-Angular Stack

## Getting Started

### Prerequisites

- Node.js (version 14 or higher)
- npm (Node Package Manager)
- Angular (version 17 or higher)
- Docker: Required for containerizing the application

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/KatieHarris2397/MNFA-User-Store-App.git
   cd MNFA-User-Store-App
   ```
2. **Navigate to angular/mnfa-user-store-app and install dependencies**:
   ```bash
   cd angular/mnfa-user-store-app
   npm install
   ```
3. **Create an Angular build**:
   ```bash
   ng build
   ```
4. **Build Docker container for frontend**:
   ```bash
   docker build -t mnfa-angular-user-store:latest .
   ```
5. **Navigate to fastAPI folder**:
   ```bash
   cd ../../fastAPI
   ```
6. **Build Docker container for backend**:
   ```bash
   docker build -t mnfa-fastapi-user-store:latest .
   ```
7. **Navigate to mongoDB folder**:
   ```bash
   cd ../mongoDB
   ```
8. **Build Docker container for mongoDB**:
   ```bash
   docker build -t mongodb-with-admin-access-to-db-created:latest .
