from django.contrib import admin
from .models import Book, Song, Movie, DeputyFail

admin.site.register(Book)
admin.site.register(Song)
admin.site.register(Movie)
admin.site.register(DeputyFail)

# Register your models here.
