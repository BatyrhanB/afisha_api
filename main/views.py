from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from main.models import Cinema, Movie
from rest_framework.response import Response
from .serializers import MovieSerializer

@api_view(['GET'])
def cinema_list_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def cinema_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'eror':'Movie not found'})
    serializer = MovieSerializer(movie, many=False)
    return Response(data=serializer.data)

