# Portfolio API

This is a Django REST Framework-based API for managing a portfolio, including projects and articles.

## Features

- User registration and authentication
- CRUD operations for projects
- CRUD operations for articles
- JWT-based authentication
- API documentation with drf-spectacular

## Prerequisites

- Python 3.8+
- Docker and Docker Compose (for containerized setup)
- MySQL

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/nikenhpsr/web-api.git
    cd web-api
    ```
2. Create a `.env` file in the project root and add the following variables:
    ```bash 
    DEBUG=True
    SECRET_KEY=your_secret_key_here
    DATABASE_URL=mysql://user:password@host:port/database_name
    ```
3. Build and run the Docker containers:
    ```bash
    docker-compose up --build
    ```

4. Run migrations:
    ```bash
    docker-compose exec web python manage.py migrate
    ```
## API Endpoints

- `/api/register/`: User registration
- `/api/login/`: User login (returns JWT token)
- `/api/projects/`: List and create projects
- `/api/projects/<id>/`: Retrieve, update, and delete a specific project
- `/api/articles/`: List and create articles
- `/api/articles/<id>/`: Retrieve, update, and delete a specific article

## Authentication

This API uses JWT (JSON Web Tokens) for authentication. To authenticate, include the JWT token in the Authorization header of your requests:
Authorization: Bearer <your_token_here>
Copy
## API Documentation

API documentation is available at `/api/schema/swagger-ui/` when the server is running.

## Run the Container
To run :
```docker
docker-compose exec web python manage.py test
```
