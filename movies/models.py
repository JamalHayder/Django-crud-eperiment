from django.db import models
from django.core.urlresolvers import reverse


class Movie(models.Model):
    director = models.CharField(max_length=250)
    movie_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    movie_art = models.FileField(blank=True)

    def __str__(self):
        return self.movie_title + ' - ' + self.director

    def get_absolute_url(self):
        return reverse('movies:detail', kwargs={'movie_id': self.pk})


class Cast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role = models.CharField(max_length=250)
    cast_name = models.CharField(max_length=250)

    def __str__(self):
        return self.cast_name

    def get_absolute_url(self):
        return reverse('movies:detail', kwargs={'cast_id': self.pk})


class Trivia(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    trivia_details = models.TextField(max_length=1000)

    def __str__(self):
        return self.trivia
        pass
