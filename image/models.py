from django.db import models
from image.storage import OverwriteStorage

#class ImageUploader(models.Model):
    # name=models.ImageField(upload_to='media')
    # name=models.FileField(upload_to='media')

# this will overwrite the name of the file
class ImageUploader(models.Model):
    name = models.FileField(storage=OverwriteStorage(), upload_to='media')
    # You could upload to a folder called username
