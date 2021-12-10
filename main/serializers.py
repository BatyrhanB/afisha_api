from rest_framework import serializers
from .models import Movie

class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
