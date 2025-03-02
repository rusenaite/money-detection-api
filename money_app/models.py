from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to="uploads/")
    processed_image = models.ImageField(upload_to="processed/", null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)