from django.db import models

class Genre(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return '%s' % (self.name)

class Book(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=128)
    date_started = models.DateTimeField()
    date_finished = models.DateTimeField()
    genres = models.ManyToManyField(Genre)