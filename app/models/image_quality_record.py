from sqlalchemy import Column, Integer, Float, String, Text, DateTime
from sqlalchemy.sql import func
from app.models.db import Base

class ImageQualityRecord(Base):
    __tablename__ = 'image_quality_records'

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(Text, nullable=True)
    face_count = Column(Integer, nullable=False)
    blur_score = Column(Float, nullable=False)
    quality_status = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
