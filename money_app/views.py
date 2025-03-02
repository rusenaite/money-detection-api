from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        
        # Send to FastAPI server (Docker)
        files = {"file": (file.name, file.read(), file.content_type)}
        FASTAPI_URL = "http://localhost:8001/upload"

        try:
            response = requests.post(FASTAPI_URL, files=files)
            if response.status_code == 200:
                return HttpResponse(response.content, content_type="image/jpeg")
            else:
                return JsonResponse({"error": "Model server failed"}, status=500)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)
