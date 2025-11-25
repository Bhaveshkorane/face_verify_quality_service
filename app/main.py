from fastapi import FastAPI
from app.routes.validate_image import router as validate_router

app = FastAPI(title="face verify quality service")

app.include_router(validate_router, prefix="")
