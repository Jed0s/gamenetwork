from django.shortcuts import render
import datetime

# Create your views here.
def main_page_view(request):
    return render(request, 'main_page/main_page.html')

def uniqueness_title_view(request):
    return render(request, 'main_page/uniqueness_title.html')

"""
A view function, or view for short, is a Python function that takes a Web request and returns a Web response.
"""
