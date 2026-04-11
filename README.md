# FastAPI Calculator with Secure User Model, Testing, CI/CD and Docker

A dynamic and fully tested **FastAPI-based calculator application** with a responsive UI, secure user management using **SQLAlchemy** and **Pydantic**, password hashing, PostgreSQL integration, Docker support, and automated **CI/CD** using **GitHub Actions** and **Docker Hub**.

---

## Features

### Calculator Features
- REST API built with FastAPI
- Responsive web interface
- Arithmetic operations:
  - ➕ Addition
  - ➖ Subtraction
  - ✖ Multiplication
  - ➗ Division
- Error handling for invalid operations such as divide by zero
- Logging of operations and errors

### Secure User Model Features
- SQLAlchemy `User` model
- Unique constraints on:
  - `username`
  - `email`
- Secure password storage using hashed passwords
- `created_at` timestamp for each user
- Pydantic schemas for request and response validation:
  - `UserCreate`
  - `UserRead`

### Testing
- Unit tests for calculator operations
- Unit tests for password hashing and verification
- Schema validation tests
- Integration tests for user endpoints and database constraints
- End-to-end UI test using Playwright

### CI/CD
- Automated testing with GitHub Actions
- PostgreSQL service container used during CI integration tests
- Docker image build and push to Docker Hub after successful test execution

---

## Technologies Used

- Python 3.11
- FastAPI
- SQLAlchemy
- Pydantic
- PostgreSQL
- Psycopg
- Pytest
- Playwright
- Docker
- Docker Compose
- GitHub Actions
- Docker Hub

---

## Project Structure

```text
fastapi-calculator/
│
├── app/
│   ├── main.py
│   ├── operations.py
│   ├── logger.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── security.py
│
├── tests/
│   ├── test_api.py
│   ├── test_operations.py
│   ├── test_schemas.py
│   ├── test_security.py
│   └── test_users_integration.py
│
├── e2e/
│   └── test_e2e.py
│
├── .github/workflows/
│   └── ci-cd.yml
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pytest.ini
├── app.log
├── README.md
└── reflection.md
````

---

## API Endpoints

### Calculator Endpoints

* `GET /` → Home route
* `GET /add?a=5&b=3`
* `GET /subtract?a=10&b=4`
* `GET /multiply?a=6&b=2`
* `GET /divide?a=20&b=5`

### User Endpoints

* `POST /users` → Create a new user
* `GET /users/{user_id}` → Get user by ID

---

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/ttreddy2911/fastapi-calculator.git
cd fastapi-calculator
```

### 2. Create and activate a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
playwright install
```

### 4. Make sure PostgreSQL is available

You can either:

* run PostgreSQL locally, or
* use Docker Compose

Set your database connection string as an environment variable.

#### Windows PowerShell

```powershell
$env:DATABASE_URL="postgresql+psycopg://postgres:postgres@localhost:5432/fastapi_db"
```

#### macOS/Linux

```bash
export DATABASE_URL="postgresql+psycopg://postgres:postgres@localhost:5432/fastapi_db"
```

### 5. Run the application

```bash
uvicorn app.main:app --reload
```

### 6. Open in browser

#### Calculator UI

```text
http://127.0.0.1:8000/calculator
```

#### Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

## Run with Docker

### Build and start the application with PostgreSQL

```bash
docker compose up --build
```

### Open in browser

#### Calculator UI

```text
http://localhost:8000/calculator
```

#### Swagger UI

```text
http://localhost:8000/docs
```

---

## Run Tests Locally

Run all tests:

```bash
python -m pytest -v
```

Expected result:

```text
21 passed
```

This includes:

* calculator API tests
* operations tests
* schema validation tests
* hashing tests
* integration tests for users
* Playwright E2E test

---

## Test Cases Covered

### Unit Tests

* Addition
* Subtraction
* Multiplication
* Division
* Divide by zero
* Password hashing
* Password verification
* Pydantic schema validation

### Integration Tests

* Create user successfully
* Reject duplicate username
* Reject duplicate email
* Reject invalid email input

### E2E Test

* Calculator UI interaction using Playwright

---

## Secure User Model

The application includes a secure `User` model with the following fields:

* `id`
* `username`
* `email`
* `password_hash`
* `created_at`

### Security Notes

* Raw passwords are **never stored**
* Passwords are hashed before saving to the database
* API responses do **not** expose `password_hash`

---

## GitHub Actions CI/CD

The GitHub Actions workflow is configured to:

* run automatically on push and pull request
* install project dependencies
* start a PostgreSQL service container
* run all unit, integration, and E2E tests
* build and push a Docker image to Docker Hub after successful tests

### Workflow Status

* Unit tests: Passing
* Integration tests: Passing
* E2E tests: Passing
* Docker build: Passing
* Docker Hub push: Passing

---

## Docker Hub Repository

Replace this with your actual Docker Hub image link:

```text
https://hub.docker.com/r/tippireddy/fastapi-calculator
```

Example pull command:

```bash
docker pull tippireddy/fastapi-calculator:latest
```

---

## Screenshots

### 1. Application UI

Responsive calculator interface running in the browser.

![Application UI](FastAPI_UI.png)

---

### 2. Swagger API

FastAPI Swagger documentation showing calculator and user endpoints.

![Swagger UI](SwaggerUI.png)

---

### 3. Test Results

Terminal screenshot showing all tests passing locally.

![Test Results](Tests.PNG)

---

### 4. GitHub Actions Workflow

Successful GitHub Actions pipeline run.

![GitHub Actions](GitHubActions.png)

---

### 5. Docker Hub Deployment

Docker Hub repository page showing the pushed image.

![Docker Hub](DockerHub.png)

---

## Logging

Logs are stored in:

```text
app.log
```

The application logs:

* calculator operations
* divide-by-zero errors
* user creation events
* duplicate user/email errors

---

## Reflection

This project was extended from a calculator API into a more complete FastAPI application with:

* secure user data modeling
* database integration
* password hashing
* robust testing
* automated CI/CD
* Docker containerization

A separate reflection document is included in:

```text
reflection.md
```

It discusses:

* implementation experience
* development challenges
* Docker and CI/CD setup issues
* testing strategy
* lessons learned

---

## How to Verify the Project

### Local Verification

1. Run PostgreSQL
2. Start the app with `uvicorn`
3. Open `/docs`
4. Test calculator endpoints
5. Test `POST /users`
6. Test duplicate username/email validation
7. Run `python -m pytest -v`

### Docker Verification

1. Run `docker compose up --build`
2. Open `http://localhost:8000/docs`
3. Test calculator and user endpoints
4. Confirm app connects to PostgreSQL

### CI/CD Verification

1. Push code to GitHub
2. Open the **Actions** tab
3. Confirm the workflow passes
4. Check Docker Hub for the pushed image

---

## Author

**T. T. Reddy**
GitHub Repository:

```text
https://github.com/ttreddy2911/fastapi-calculator
```

---

## License

This project is for educational and academic purposes.

````

```text
tippireddy
````

