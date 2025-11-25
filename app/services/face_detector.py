import face_recognition
from PIL import Image
import numpy as np
from io import BytesIO

def detect_faces(image_bytes: bytes, model: str = 'hog') -> int:
    img = Image.open(BytesIO(image_bytes)).convert('RGB')
    arr = np.array(img)
    locations = face_recognition.face_locations(arr, model=model)
    return len(locations)
