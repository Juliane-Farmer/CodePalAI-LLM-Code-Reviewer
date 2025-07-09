from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_review_valid_python_code():
    response = client.post("/review", json={"code": "print('Hello')", "language": "Python"})
    assert response.status_code == 200, "Expected status code 200 for valid input"
    assert "Issue Summary" in response.json()["result"], "'Issue Summary' not found in response for valid code"

def test_review_empty_code():
    response = client.post("/review", json={"code": "", "language": "Python"})
    assert response.status_code == 200, "Expected status code 200 for empty code input"
    assert response.json()["result"] != "", "Expected some response content for empty code input"

def test_review_missing_language_field():
    response = client.post("/review", json={"code": "print('Hello')"})
    assert response.status_code == 422, "Expected status code 422 when 'language' field is missing"

def test_review_invalid_language():
    response = client.post("/review", json={"code": "print('Hello')", "language": "InvalidLang"})
    assert response.status_code == 200, "Expected status code 200 for invalid language input"
    assert "Issue Summary" in response.json()["result"], "'Issue Summary' missing for invalid language"

def test_review_missing_code_field():
    response = client.post("/review", json={"language": "Python"})
    assert response.status_code == 422, "Expected status code 422 when 'code' field is missing"

def test_review_non_string_code():
    response = client.post("/review", json={"code": 12345, "language": "Python"})
    assert response.status_code == 422, "Expected status code 422 for non-string code value"
