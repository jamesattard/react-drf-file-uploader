from django.shortcuts import render
from requests import Response
from rest_framework import viewsets, generics, renderers, status
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.views import APIView
from image.serializer import ImageUploaderSerializer
from image.models import ImageUploader

# Works
# class ImageUploaderView(generics.ListCreateAPIView):
#   """List all documents on server and create new"""
#   queryset = ImageUploader.objects.all()
#   serializer_class = ImageUploaderSerializer

class ImageUploaderView(viewsets.ModelViewSet):
    renderer_classes = [renderers.JSONRenderer]
    queryset = ImageUploader.objects.all()
    serializer_class = ImageUploaderSerializer
    parser_classes = (MultiPartParser,FileUploadParser,)

    def perform_create(self, serializer):
        print "Filename: ", self.request.data.get('name')
        serializer.save()
