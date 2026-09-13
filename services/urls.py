from django.urls import path
from . import views

urlpatterns = [
  path('', views.services_index, name='services_index'),
]