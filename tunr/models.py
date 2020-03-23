from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name


class Song(models.Model):
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='songs')
    title = models.CharField(max_length=100)
    album = models.CharField(max_length=100, null=True, blank=True)
    year = models.CharField(max_length=10)

    def __str__(self):
        return self.title
