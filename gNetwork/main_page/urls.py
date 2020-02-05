from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page_view, name='main_page_url'),
    url(r'uniqueness_title/', views.uniqueness_title_view, name='uniqueness_title_url'),
]