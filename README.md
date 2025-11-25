# Face Verify Quality Service

This service checks an uploaded image for exactly one human face and also calculates a blur score for the image.  
It is built with FastAPI, face-recognition, and OpenCV.

The service exposes one endpoint:

```
POST /face-quality/validate
```

## Features

- Accept an image upload using form data  
- Detect number of faces in the image  
- Return:
  - success or failure  
  - message  
  - faceCount  
  - blurScore  
  - qualityStatus  
- Save accepted image quality details in the database  
- SQLite used by default and PostgreSQL supported  

---

# Setup and Run

## 1. Create a virtual environment

### Windows
```
python -m venv venv
venv\Scripts\activate
```

### Mac / Linux
```
python3 -m venv venv
source venv/bin/activate
```

---

## 2. Install system dependencies

### Ubuntu
```
sudo apt update
sudo apt install -y build-essential cmake libopenblas-dev liblapack-dev libx11-dev libgtk-3-dev libboost-all-dev
```

### Mac
```
brew install cmake boost
```

---

## 3. Install Python packages

```
pip install -r requirements.txt
```

---

## 4. Run the service

```
uvicorn app.main:app --reload
```

The service starts at:

```
http://127.0.0.1:8000
```

---

# API Usage

## POST /face-quality/validate

### Request
- Content-Type: multipart/form-data  
- Field name: `file`

### Curl Example

```
curl -X POST "http://127.0.0.1:8000/face-quality/validate" \
  -F "file=@/path/to/image.jpg"
```

---

# Running Tests

```
pytest -q
```

Place sample images inside:

```
tests/data/
```

---

# Database

The service uses SQLite by default.  
To use PostgreSQL:

```
export DATABASE_URL=postgresql://user:pass@localhost:5432/mydb
```

Restart the service after updating.
