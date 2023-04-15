from rest_framework import serializers
from .models import Effmodel
from .models import SaveImageModel



class EffmodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Effmodel
        fields = (
            'id',
            'title',
            'content',
        )

class SaveImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaveImageModel
        fields = (
            'updated_at',
            'image'
        )
