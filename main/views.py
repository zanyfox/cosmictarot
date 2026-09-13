from django.shortcuts import render
#from django.http import HttpResponse
from .forms import PostForm

# Create your views here.

def index(request):
  return render(request, 'main/index.html', {
    'page': 'index',
    'title': 'Главная страница',
    'hero': {
      'title': 'Discover Your Destiny Through the Wisdom of the Cards',
      'description': 'Your Answers Are Written in the Stars – Let\'s Reveal Them!',
      'slides': ['1.png', '2.png', '3.png'],
    }
  })
  #return HttpResponse("Hello, world. You're at the main index.")

def about(request):

  data = {
    'page': 'about',
    'title': 'О нас',
  }

  return render(request, 'main/about.html', data)
  #return HttpResponse("Hello, world. You're at the main about.")

def contact(request):

  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      form.save()
      #return redirect('index')
      return render(request, 'main/contact.html', {
        'page': 'contact',
        'title': 'Контакты',
        'success': True,
      })
    else:
      return render(request, 'main/contact.html', {
        'page': 'contact',
        'title': 'Контакты',
        'form': form,
      })

  #form = PostForm()

  return render(request, 'main/contact.html', {
    'page': 'contact',
    'title': 'Контакты'
  })
