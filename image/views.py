from django.shortcuts import render
from rest_framework import viewsets, renderers
from image.serializer import ImageUploaderSerializer
from image.models import ImageUploader

class ImageUploaderView(viewsets.ModelViewSet):
    renderer_classes = [renderers.JSONRenderer]
    queryset = ImageUploader.objects.all()
    serializer_class = ImageUploaderSerializer




