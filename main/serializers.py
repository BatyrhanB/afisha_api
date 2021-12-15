from rest_framework import serializers
from .models import Cinema, Genre, Movie, Review


class CinemaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cinema
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'
class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    genres = GenreSerializer(many=True)
    cinema = CinemaSerializer(many=False)

    class Meta:
        model = Movie
        fields = 'id title reviews genres cinema'.split()
