from django.shortcuts import render
from .models import Post

from django.views.generic import DetailView

# Create your views here.

def blog_index(request):
  posts = Post.objects.order_by('-date')[:3] #.all()
  return render(request, 'blog/index.html', {
    'title': 'Блог',
    'posts': posts
  })

class PostDetail(DetailView):
  model = Post
  template_name = 'blog/detail.html'
  context_object_name = 'post'