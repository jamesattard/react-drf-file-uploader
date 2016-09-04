from django.shortcuts import render
from requests import Response
from rest_framework import viewsets, renderers
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from image.serializer import ImageUploaderSerializer
from image.models import ImageUploader

class ImageUploaderView(viewsets.ModelViewSet):
    renderer_classes = [renderers.JSONRenderer]
    queryset = ImageUploader.objects.all()
    serializer_class = ImageUploaderSerializer
    parser_classes = (MultiPartParser,)

    # def create(self, request, *args, **kwargs):
    #     print "request"
    #     print request.data
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     print "hey done "
    #     headers = self.get_success_headers(serializer.data)
    #     print "hey done 2"
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def perform_create(self, serializer):
    #     serializer.save()





