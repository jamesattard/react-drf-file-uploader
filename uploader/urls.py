from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from django.conf.urls import include


from image.views import  ImageUploaderView
from uploader.home_view import index

external_router = routers.DefaultRouter()

external_router.register(r'image', ImageUploaderView)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^api/v0/', ImageUploaderView.as_view(), name="imageuploader"),
    url(r'^api/v0/',include(external_router.urls,namespace='v0')),
    url(r'^$',index)
]
