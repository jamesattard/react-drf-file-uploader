from django.db import models

# Create your models here.

class ImageUploader(models.Model):
    name=models.ImageField(upload_to='media')

