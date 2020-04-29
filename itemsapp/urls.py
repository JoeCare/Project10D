from django.urls import path, include  # url
from . import views

urlpatterns = [
    # url(r'^$', view.index),
    path('home', views.home),
    path('', views.home),
]
