from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from app.services.face_detector import detect_faces
from app.services.blur_calculator import compute_blur_score
from app.services.recorder import record_quality

router = APIRouter()

def build_response(success: bool, message: str, face_count: int, blur_score: float, quality_status: str):
    return JSONResponse(status_code=200, content={
        "success": success,
        "message": message,
        "data": {
            "faceCount": face_count,
            "blurScore": round(float(blur_score), 2),
            "qualityStatus": quality_status
        }
    })

@router.post("/face-quality/validate")
async def validate_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        return build_response(False, "Invalid or unsupported image.", 0, 0.0, "REJECTED")

    contents = await file.read()

    try:
        face_count = detect_faces(contents)
    except Exception:
        return build_response(False, "Invalid or unsupported image.", 0, 0.0, "REJECTED")

    try:
        blur_score = compute_blur_score(contents)
    except Exception:
        blur_score = 0.0

    if face_count == 0:
        return build_response(False, "No face detected.", 0, blur_score, "REJECTED")
    if face_count > 1:
        return build_response(False, "Multiple faces detected.", face_count, blur_score, "REJECTED")

    record_quality(filename=getattr(file, 'filename', None), face_count=face_count, blur_score=blur_score)
    return build_response(True, "Image accepted.", face_count, blur_score, "RECORDED")
