from rest_framework import serializers
from image.models import ImageUploader

class ImageUploaderSerializer(serializers.ModelSerializer):
    print "hey in here"
    class Meta:
        model = ImageUploader

