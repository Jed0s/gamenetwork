from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'cool_stuff/widgets/$', views.widgets_view, name='widgets_url'),
]