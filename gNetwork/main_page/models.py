from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, blank=True, help_text="optional")

    def __str__(self):
        return self.title

class Movie(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, blank=True, help_text="optional")

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, blank=True, help_text="optional")

    def __str__(self):
        return self.title

class DeputyFail(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    consigment = models.CharField(max_length=100)
    fail_date = models.DateField()
    fail = models.TextField()

    def __str__(self):
        return self.name

"""
A model is the single, definitive source of information about your data.


LINKS:
  https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Models
"""
