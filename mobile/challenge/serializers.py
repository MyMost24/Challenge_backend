from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Challenge, Video


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email']


class VideoSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Video
        fields = ['id', 'name', 'video', 'image', 'user']


class ChallengeSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, required=False)

    class Meta:
        model = Challenge
        fields = ['id', 'name', 'description', 'image', 'videos']
