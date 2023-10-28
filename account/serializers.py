from rest_framework import serializers
from .models import User


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name", 'phone', 'massage', 'address', 'text', 'Image']
