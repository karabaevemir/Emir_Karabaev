from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Director, Movie, Review
from movie_app.serializers import MovieSerializers, DirectorSerializers, ReviewSerializers, MovieReviewSerializer
from rest_framework import status


@api_view(['GET'])
def movies_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()

        serializer = MovieSerializers(movies, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def movies_detail_view(request, **kwargs):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(id=kwargs['id'])
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializers(movie, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def directors_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()

        serializer = DirectorSerializers(directors, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def directors_detail_view(request, **kwargs):
    if request.method == 'GET':
        try:
            director = Director.objects.get(id=kwargs['id'])
        except Director.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DirectorSerializers(director, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def reviews_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()

        serializer = MovieSerializers(reviews, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def reviews_detail_view(request, **kwargs):
    if request.method == 'GET':
        try:
            review = Review.objects.get(id=kwargs['id'])
        except Review.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewSerializers(review, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def review_movies_view(request):
    if request.method == "GET":
        movie = Movie.objects.all()
        serializer = MovieReviewSerializer(movie, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

