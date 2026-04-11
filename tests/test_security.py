from app.security import hash_password, verify_password

def test_hash_password_changes_plain_text():
    raw = "supersecret123"
    hashed = hash_password(raw)

    assert hashed != raw
    assert isinstance(hashed, str)

def test_verify_password_success():
    raw = "supersecret123"
    hashed = hash_password(raw)

    assert verify_password(raw, hashed) is True

def test_verify_password_failure():
    hashed = hash_password("supersecret123")

    assert verify_password("wrongpassword", hashed) is False