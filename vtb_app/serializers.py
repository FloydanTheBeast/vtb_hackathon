from django.contrib.auth.models import User, Group
from rest_framework import serializers


class TestSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=100)


class CarRecognizeSerializer(serializers.Serializer):
    photo = serializers.ImageField()
