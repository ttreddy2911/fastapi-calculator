#  FastAPI Calculator with Testing & CI

A dynamic and fully tested **FastAPI-based calculator application** with a responsive UI, complete test coverage, logging and automated CI using GitHub Actions.

---

##  Features

* ✅ REST API built with FastAPI
* ✅ Responsive Web Interface
* ✅ Arithmetic Operations:

  * ➕ Addition
  * ➖ Subtraction
  * ✖ Multiplication
  * ➗ Division
* ✅ Error handling (e.g., divide by zero)
* ✅ Logging of operations and errors
* ✅ Full Testing:

  * Unit Tests (Pytest)
  * Integration Tests (API endpoints)
  * End-to-End Tests (Playwright)
* ✅ Continuous Integration (CI) with GitHub Actions

---

## 🛠️ Technologies Used

* Python 3.10 / 3.11
* FastAPI
* Pytest
* Playwright
* GitHub Actions

---

## 📂 Project Structure

```
fastapi-calculator/
│
├── app/
│   ├── main.py
│   ├── operations.py
│   └── logger.py
│
├── tests/
│   ├── test_api.py
│   └── test_operations.py
│
├── e2e/
│   └── test_e2e.py
│
├── .github/workflows/
│   └── test.yml
│
├── requirements.txt
├── pytest.ini
├── app.log
└── README.md
```

---

## ▶️ Run Locally

### 1. Clone the repository

```
git clone https://github.com/ttreddy2911/fastapi-calculator.git
cd fastapi-calculator
```

### 2. Install dependencies

```
pip install -r requirements.txt
playwright install
```

### 3. Run the application

```
uvicorn app.main:app --reload
```

👉 Open in browser:

Calculator UI

```
http://127.0.0.1:8000/calculator
```
API Documentation (Swagger UI)

```
http://127.0.0.1:8000/docs
```
---

## 🧪 Run Tests

```
python -m pytest
```

✔ Expected Output:

```
12 passed
```

---

## ⚙️ GitHub Actions (CI)

* Runs automatically on every push
* Executes all tests (unit + integration + E2E)
* Ensures application stability

✔ Status: **Passing ✅**

---

## 📸 Screenshots

### Application UI

Shows responsive calculator interface with operations.

### Swagger API

Demonstrates FastAPI endpoints and responses.

### Test Results

All tests passing successfully (12/12).

### GitHub Actions

CI pipeline running and passing successfully.

---

## 📊 Logging

* Logs stored in `app.log`
* Tracks:

  * Operations performed
  * Errors (e.g., divide by zero)


