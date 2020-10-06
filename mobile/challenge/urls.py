from django.urls import path, include
from rest_framework import routers
from challenge import views

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register('video', views.VideoViewset)
router.register('user', views.UserViewset)
router.register('challenge', views.ChallengeViewset)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
