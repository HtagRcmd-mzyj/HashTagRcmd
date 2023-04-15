from rest_framework import serializers
from .models import Crawlingmodel
from .models import SaveImageModel2

class CrawlingmodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crawlingmodel
        fields = (
            'id',
            'keyword',
            'hashtag',
            #'hashtag_loc'
        )

class SaveImageModelSerializer2(serializers.ModelSerializer):
    class Meta:
        model = SaveImageModel2
        fields = (
            'updated_at',
            'image'
        )
