from django.urls import path
from . import views

urlpatterns = [
  path('', views.services_index, name='services_index'),
  path('<slug:slug>', views.service_detail, name='service_detail'),
]