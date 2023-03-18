from dataclasses import field
from rest_framework.serializers import ModelSerializer
from .models import note


class note_serializer(ModelSerializer):
    class Meta:
        model = note
        fields = '__all__'
