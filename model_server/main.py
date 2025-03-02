from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import cv2
import numpy as np
from ultralytics import YOLO
import os

app = FastAPI()

PROCESSED_DIR = "media"
os.makedirs(PROCESSED_DIR, exist_ok=True)

MODEL_PATH = "model/best.pt"
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")

model = YOLO(MODEL_PATH)

@app.post("/upload/")
async def process_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    nparr = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    results = model(image)

    for result in results:
        for box in result.boxes.xyxy:
            x1, y1, x2, y2 = map(int, box)
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 3)

    processed_image_path = os.path.join(PROCESSED_DIR, "processed_image.jpg")
    cv2.imwrite(processed_image_path, image)

    return FileResponse(processed_image_path, media_type="image/jpeg")

@app.get("/")
def home():
    return {"message": "FastAPI YOLO model is running"}
