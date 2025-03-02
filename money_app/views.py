import cv2
import torch
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.files.storage import default_storage
from django.conf import settings
import os
from ultralytics import YOLO

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Tikrasis kelias iki `best.pt`
MODEL_PATH = os.path.join(BASE_DIR, "money_app", "best.pt")  # Patikrink, ar failas čia yra

# Įkeliamas modelis
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")

model = YOLO(MODEL_PATH)

@api_view(["POST"])
def upload_image(request):
    if "image" not in request.FILES:
        return Response({"error": "No image uploaded"}, status=400)

    image_file = request.FILES["image"]
    image_path = default_storage.save("uploads/" + image_file.name, image_file)

    # Apdorojame vaizdą
    full_image_path = os.path.join(settings.MEDIA_ROOT, image_path)
    image = cv2.imread(full_image_path)
    
    if image is None:
        return Response({"Error": f"Failed to read image at {full_image_path}"}, status=500)

    results = model(full_image_path)

    # Pažymime aptiktus objektus
    for result in results:
        for box in result.boxes.xyxy:
            x1, y1, x2, y2 = map(int, box)
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 3)

    processed_path = "processed/processed_" + image_file.name
    processed_full_path = os.path.join(settings.MEDIA_ROOT, processed_path)
    print(f"Saving processed image to: {processed_full_path}")
    cv2.imwrite(processed_full_path, image, [cv2.IMWRITE_JPEG_QUALITY, 90])
    cv2.imwrite(processed_full_path, image)

    return Response({
        "original": request.build_absolute_uri(settings.MEDIA_URL + image_path),
        "processed": request.build_absolute_uri(settings.MEDIA_URL + processed_path)
    })
