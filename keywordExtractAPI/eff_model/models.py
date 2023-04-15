from django.db import models

# Create your models here.

# lets us explicitly set upload path and filename
def upload_to(instance, filename):
    return "post_images/{filename}".format(filename="test.jpg")

class SaveImageModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=upload_to, blank=True)

class Effmodel(models.Model):
    title = models.CharField(max_length=50, default='')
    content = models.TextField(default='')
