from rest_framework import serializers
from movie_app.models import Movie, Director, Review


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director')


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('name',)


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('text', 'movie')