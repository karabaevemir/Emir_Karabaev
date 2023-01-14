from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Director, Movie, Review
from movie_app.serializers import MovieSerializers, DirectorSerializers, ReviewSerializers, MovieReviewSerializer
from rest_framework import status


@api_view(['GET', 'POST'])
def movies_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializers(movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director = request.data.get('director')
        movie = Movie.objects.create(title=title, description=description, duration=duration, director=director)
        movie.save()
        return Response(data={'message': 'Data received!'})


@api_view(['GET', 'PUT', 'DELETE'])
def movies_detail_view(request, **kwargs):
    try:
        movie = Movie.objects.get(id=kwargs['id'])
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieSerializers(movie, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director = request.data.get('director')
        movie.save()
        return Response(data={'message': 'Data received!'})


@api_view(['GET', 'POST'])
def directors_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializers(directors, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        director.save()
        return Response(data={'message': 'Data received!'})


@api_view(['GET', 'PUT', 'DELETE'])
def directors_detail_view(request, **kwargs):
    try:
        director = Director.objects.get(id=kwargs['id'])
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DirectorSerializers(director, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        director.name = request.data.get('name')
        return Response(data={'message': 'Data received!'})


@api_view(['GET', 'POST'])
def reviews_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = MovieSerializers(reviews, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.data.get('text')
        movie = request.data.get('movie')
        stars = request.data.get('stars')
        review = Review.objects.create(text=text, movie=movie, stars=stars)
        review.save()
        return Response(data={'message': 'Data received!'})


@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail_view(request, **kwargs):
    try:
        review = Review.objects.get(id=kwargs['id'])
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewSerializers(review, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        review.text = request.data.get('text')
        review.movie = request.data.get('movie')
        review.stars = request.data.get('stars')
        review.save()
        return Response(data={'message': 'Data received!'})



@api_view(["GET"])
def review_movies_view(request):
    if request.method == "GET":
        movie = Movie.objects.all()
        serializer = MovieReviewSerializer(movie, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

