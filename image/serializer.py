from rest_framework import serializers
from image.models import ImageUploader

class ImageUploaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUploader

