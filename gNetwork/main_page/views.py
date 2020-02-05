from django.shortcuts import render
from .forms import BookForm, DeputyFailForm
import datetime

# Create your views here.
def main_page_view(request):
    return render(request, 'main_page/main_page.html')

def uniqueness_title_view(request):
    form = BookForm()
    return render(request, 'main_page/uniqueness_title.html', {'form': form})

def deputy_fails_view(request):
    form = DeputyFailForm() # ?
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "main_page/deputy_fails.html", context)

"""
A view function, or view for short, is a Python function that takes a Web request and returns a Web response.
"""
