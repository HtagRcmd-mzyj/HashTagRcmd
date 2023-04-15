from rest_framework import serializers
from .models import KeyBERTModel


class KeyBERTModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyBERTModel
        fields = (
            'id',
            'input_text',
            'hashtag',
            'updated_at',
        )
