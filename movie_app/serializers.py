from rest_framework import serializers
from movie_app.models import Movie, Director, Review


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director')


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name movie_count'.split()


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('text', 'movie')


class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"

    def get_reviews(self, movie):
        return [i.stars for i in movie.reviews.all()]

    def get_rating(self, movie):
        return movie.rating
