from django.db import models

# Create your models here.

class KeyBERTModel(models.Model):
    input_text = models.TextField(default='')
    hashtag = models.TextField(default='')
    updated_at = models.DateTimeField(auto_now=True)
