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
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text[:15]
