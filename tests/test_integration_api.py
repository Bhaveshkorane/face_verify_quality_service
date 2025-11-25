import pytest
from fastapi.testclient import TestClient
from app.main import app
from pathlib import Path

client = TestClient(app)
TEST_IMAGE_DIR = Path(__file__).parent / 'data'

def test_api_no_file():
    resp = client.post('/face-quality/validate')
    assert resp.status_code == 422

def test_api_invalid_mime():
    resp = client.post('/face-quality/validate', files={'file': ('text.txt', b'hello', 'text/plain')})
    assert resp.status_code == 200
    body = resp.json()
    assert body['success'] is False
    assert body['message'] == 'Invalid or unsupported image.'

def test_api_one_face():
    with open(TEST_IMAGE_DIR / 'one_face.jpg', 'rb') as f:
        resp = client.post('/face-quality/validate', files={'file': ('one_face.jpg', f, 'image/jpeg')})
    assert resp.status_code == 200
    body = resp.json()
    assert body['success'] is True
    assert body['data']['faceCount'] == 1
