from django.urls import path
from . import views

urlpatterns = [
  path('', views.blog_index, name='blog_index'),
  path('<int:pk>', views.PostDetail.as_view(), name='post_detail'),
]
