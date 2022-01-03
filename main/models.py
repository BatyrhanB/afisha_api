from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):

        return self.name 
class Cinema(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class Movie(models.Model):
    image = models.ImageField(upload_to='products', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre, blank=True, null=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                                 related_name='reviews')
    def __str__(self):
        return self.text

