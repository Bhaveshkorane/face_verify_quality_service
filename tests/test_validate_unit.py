import pytest
from app.services.blur_calculator import compute_blur_score
from app.services.face_detector import detect_faces
from pathlib import Path

TEST_IMAGE_DIR = Path(__file__).parent / 'data'

def load_image(path: Path) -> bytes:
    return path.read_bytes()

def test_blur_score_calculation():
    b = load_image(TEST_IMAGE_DIR / 'one_face.jpg')
    score = compute_blur_score(b)
    assert isinstance(score, float)
    assert score >= 0

def test_face_detection_one_face():
    b = load_image(TEST_IMAGE_DIR / 'one_face.jpg')
    count = detect_faces(b)
    assert count == 1

def test_face_detection_no_face():
    b = load_image(TEST_IMAGE_DIR / 'no_face.jpg')
    count = detect_faces(b)
    assert count == 0
