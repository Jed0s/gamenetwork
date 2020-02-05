from django import forms
from .models import Book, Song, Movie

class BookForm(forms.Form):
    class Meta:
        model = Book
        fields = ('title', 'author', 'genre')

"""
LINKS:
  https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Forms
"""