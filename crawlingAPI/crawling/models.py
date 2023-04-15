from django.db import models

# Create your models here.
def upload_to(instance, filename):
    return 'post_images/{filename}'.format(filename='test.jpg')


class SaveImageModel2(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=upload_to, blank=True)
    class Meta:
        db_table = "saveimagemodel2"

class Crawlingmodel(models.Model):
    keyword = models.CharField(max_length=50, default='')
    hashtag = models.TextField(default='')
    #hashtag_loc = models.TextField(default='')
    class Meta:
        db_table = "crawlingmodel"
