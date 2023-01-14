from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from movie_app.models import Movie, Director, Review


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id username first_name last_name email'.split()


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director')


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(required=True)
    duration = serializers.IntegerField(required=True)
    director_id = serializers.IntegerField(required=True, min_value=1)

    def validate_title(self, title):
        title_exists = Movie.objects.filter(title=title).exists()
        if not title_exists:
            return title
        raise ValidationError('Уже есть')

    def validate_director_id(self, director_id):
        director_exists = Director.objects.filter(id=director_id).exists()
        if not director_exists:
            raise ValidationError('Уже есть')
        return director_id


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name movie_count'.split()


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=25, required=True)

    def validate_name(self, name):
        name_exists = Director.objects.filter(name=name).exists()
        if not name_exists:
            return name
        raise ValidationError('Уже есть!')


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('text', 'movie')


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=10, required=True)
    stars = serializers.IntegerField(min_value=1, max_value=5, required=True)
    movie_id = serializers.IntegerField(min_value=1, required=True)

    def validate_movie_id(self, movie_id):
        movie_exists = Movie.objects.filter(id=movie_id).exists()
        if movie_exists:
            return movie_id
        raise ValidationError('Уже есть!')


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
