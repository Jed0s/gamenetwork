from django import forms
from .models import Book, Song, Movie, DeputyFail

TITLE_BOOK = 0
TITLE_SONG = 1
TITLE_MOVIE = 2
CHOICES_TITLE = ((TITLE_BOOK, ('Book')),
                 (TITLE_SONG, ('Song')),
                 (TITLE_MOVIE, ('Movie')))

class TitleForm(forms.Form):
    category = forms.IntegerField(widget=forms.RadioSelect(choices=CHOICES_TITLE))

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