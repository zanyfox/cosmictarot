from django.shortcuts import render, get_object_or_404
from .models import Post
from services.models import Service

# Create your views here.

def blog_index(request):
  posts = Post.objects.order_by('-date')[:3] #.all()
  return render(request, 'blog/index.html', {
    'title': 'Блог',
    'page': 'blog',
    'posts': posts,
    'services': Service.objects.all()
  })

def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  posts = Post.objects.order_by('-date')[:3] #.all()
  return render(request, 'blog/detail.html', {
    'title': 'Блог',
    'page': 'blog',
    'post': post,
    'posts': posts,
    'services': Service.objects.all()
  })
