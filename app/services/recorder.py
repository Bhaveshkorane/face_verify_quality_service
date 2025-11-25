from app.models.db import get_session, init_db
from app.models.image_quality_record import ImageQualityRecord

init_db()

def record_quality(filename: str, face_count: int, blur_score: float):
    session = get_session()
    try:
        rec = ImageQualityRecord(filename=filename, face_count=face_count, blur_score=blur_score, quality_status='RECORDED')
        session.add(rec)
        session.commit()
    except Exception:
        session.rollback()
    finally:
        session.close()
