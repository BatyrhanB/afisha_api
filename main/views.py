from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from main.models import Movie
from .serializers import MovieSerializer 


class MovieListAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination

class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'


# @api_view(['GET', 'POST'])  
# def cinema_list_view(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(data=serializer.data)
#     elif request.method == 'POST':
#         serializer = MovieCreateValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
#             data={'messege': 'error',
#             'errors': serializer.errors})
#         title = request.data['title']
#         description = request.data['description']
#         cinema = request.data['cinema']
#         genres = request.data['genres']
#         movie = Movie.objects.create(
#             title=title, description=description, cinema_id=cinema,
#         )
#         movie.save()
#         movie.genres.set(genres)
#         movie.save()
#         return Response("Movie created!")

# @api_view(['GET', 'PUT', 'DELETE'])
# def cinema_detail_view(request, id):
#     try:
#         movie = Movie.objects.get(id=id)
#     except Movie.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND,
#                         data={'eror':'Movie not found'})
#     if request.method == 'GET':
#         serializer = MovieSerializer(movie, many=False)
#         return Response(data=serializer.data)
#     elif request.method == 'PUT':
#         movie.title == request.data['title']
#         movie.description == request.data['description']
#         movie.cinema == request.data['cinema']
#         movie.genres.set(request.data['genres'])
#         movie.save()
#         return Response(data={'massage': 'Movie updated!'})
#     else:
#         movie.delete()
#         return Response()


