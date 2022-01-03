from rest_framework.exceptions import ValidationError
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
    review_count = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title image reviews review_count genres cinema'.split()

    def get_review_count(self, product):
        return product.reviews.all().count()


class MovieCreateValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=500)
    description = serializers.CharField()
    cinema = serializers.IntegerField()
    genres = serializers.ListField()

    def validate_cinema(self, cinema):
        try:
            Cinema.objects.get(id=cinema)
        except Cinema.DoesNotExist:
            raise ValidationError("This ID of cinema does not exist!")
    
    def validate_title(self, title):
        if Movie.objects.filter(title=title):
            raise ValidationError('Title must be unique !')