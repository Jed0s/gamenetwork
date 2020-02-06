from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page_view, name='main_page_url'),
    url(r'uniqueness_title/$', views.uniqueness_title_view, name='uniqueness_title_url'),
    url(r'deputy_fails/$', views.deputy_fails_view, name="deputy_fails_url"),
    url(r'title(?P<choice>\d+)/$', views.selected_title_view, name='selected_title_url'),
]