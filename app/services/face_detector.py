import face_recognition
from PIL import Image
import numpy as np
from io import BytesIO


# hog model -- faster but less accurate
def detect_faces(image_bytes: bytes, model: str = 'hog') -> int:
    img = Image.open(BytesIO(image_bytes)).convert('RGB')
    arr = np.array(img)
    locations = face_recognition.face_locations(arr, model=model)
    return len(locations)


#with upsample -- best accuracy but slower
# def detect_faces(image_bytes: bytes):
#     img = Image.open(BytesIO(image_bytes)).convert('RGB')
#     arr = np.array(img)

#     # Try CNN first
#     locations = face_recognition.face_locations(arr, model='cnn', number_of_times_to_upsample=2)

#     # Fallback to HOG if nothing detected
#     if len(locations) == 0:
#         locations = face_recognition.face_locations(arr, model='hog', number_of_times_to_upsample=2)

#     return len(locations)


# # without upsample good speed and accuracy
# def detect_faces(image_bytes: bytes):
#     print("without upsample with cnn and fallback to hog")
#     img = Image.open(BytesIO(image_bytes)).convert('RGB')
#     arr = np.array(img)

#     # Try CNN first
#     locations = face_recognition.face_locations(arr, model='cnn')

#     # Fallback to HOG if nothing detected
#     if len(locations) == 0:
#         locations = face_recognition.face_locations(arr, model='hog')
        

#     return len(locations)