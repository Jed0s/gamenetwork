from django import forms
from .models import Book, Song, Movie, DeputyFail

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'genre')


class DeputyFailForm(forms.ModelForm):
    class Meta:
        model = DeputyFail
        fields = ('name', 'surname', 'consigment', 'fail_date', 'fail')

"""
LINKS:
  https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Forms
"""