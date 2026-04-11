import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db

TEST_DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://postgres:postgres@localhost:5432/fastapi_db"
)

engine = create_engine(TEST_DATABASE_URL, future=True, pool_pre_ping=True)
TestingSessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    future=True
)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(autouse=True)
def reset_db():
    db = TestingSessionLocal()
    try:
        db.execute(text("TRUNCATE TABLE users RESTART IDENTITY CASCADE;"))
        db.commit()
        yield
    finally:
        db.close()


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


def test_create_user_success(client):
    response = client.post("/users", json={
        "username": "alice",
        "email": "alice@example.com",
        "password": "password123"
    })

    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "alice"
    assert data["email"] == "alice@example.com"
    assert "password_hash" not in data


def test_duplicate_username(client):
    payload1 = {
        "username": "alice",
        "email": "alice@example.com",
        "password": "password123"
    }
    payload2 = {
        "username": "alice",
        "email": "alice2@example.com",
        "password": "password123"
    }

    client.post("/users", json=payload1)
    response = client.post("/users", json=payload2)

    assert response.status_code == 400
    assert response.json()["detail"] == "Username already exists"


def test_duplicate_email(client):
    payload1 = {
        "username": "alice",
        "email": "alice@example.com",
        "password": "password123"
    }
    payload2 = {
        "username": "bob",
        "email": "alice@example.com",
        "password": "password123"
    }

    client.post("/users", json=payload1)
    response = client.post("/users", json=payload2)

    assert response.status_code == 400
    assert response.json()["detail"] == "Email already exists"


def test_invalid_email_rejected(client):
    response = client.post("/users", json={
        "username": "bademail",
        "email": "not-an-email",
        "password": "password123"
    })

    assert response.status_code == 422