from django.urls import path

from dashboard import views

path('', views.index, name='home'),