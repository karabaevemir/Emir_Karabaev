from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *


# Create your views here.
class DirectorViewSet(ModelViewSet):
    serializer_class = DirectorSerializers
    queryset = Director.objects.all()
    authentication_classes = [IsAuthenticatedOrReadOnly]


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    permission_classes = IsAuthenticatedOrReadOnly

    @action(['GET'], detail=False)
    def reviews(self, request, *args, **kwargs):
        serializer = MovieReviewSerializer(self.get_queryset(), many=True)
        return Response(data=serializer.data)


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]

