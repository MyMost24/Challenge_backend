from django.shortcuts import render
from django.http import HttpResponse
from .serializers import VideoSerializer, ChallengeSerializer, UserSerializer
from .models import Video, Challenge
from rest_framework import viewsets
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

def index(request):
    return HttpResponse('hello world')

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class VideoViewset(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class ChallengeViewset(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    filter_backends =[DjangoFilterBackend]

