from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .views import *

ROUTER = SimpleRouter()
ROUTER.register('movies', MovieViewSet)
ROUTER.register('directors', DirectorViewSet)
ROUTER.register('reviews', ReviewViewSet)
urlpatterns = [
    path('', include(ROUTER.urls))
]