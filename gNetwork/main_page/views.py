from django.shortcuts import render
from .forms import TitleForm, DeputyFailForm
import datetime

# Create your views here.
def main_page_view(request):
    return render(request, 'main_page/main_page.html')

def uniqueness_title_view(request):
    categories = TitleForm()
    return render(request, 'main_page/uniqueness_title.html', {'categories': categories})

def selected_title_view(request, choice):
    pass

def deputy_fails_view(request):
    form = DeputyFailForm() # ?
    if form.is_valid():
        form.save()

    context = {
        'form': form,
    }
    return render(request, "main_page/deputy_fails.html", context)

"""
A view function, or view for short, is a Python function that takes a Web request and returns a Web response.
"""
