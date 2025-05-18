from django.db import models
from django.contrib.auth.models import User


class Artist(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    biography = models.TextField(max_length=200)

    def __str__(self):
        return self.name + " " + self.country


class Exhibition(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Artwork(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='artworks/', blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.title + " " + self.artist.name
