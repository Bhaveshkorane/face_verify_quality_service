import cv2
import numpy as np
from PIL import Image
from io import BytesIO

def compute_blur_score(image_bytes: bytes) -> float:
    img = Image.open(BytesIO(image_bytes)).convert('L')
    arr = np.array(img)
    h, w = arr.shape
    max_side = max(w, h)
    if max_side > 1024:
        scale = 1024.0 / float(max_side)
        new_w = int(w * scale)
        new_h = int(h * scale)
        arr = cv2.resize(arr, (new_w, new_h))
    lap = cv2.Laplacian(arr, cv2.CV_64F)
    var = float(lap.var())
    return var
