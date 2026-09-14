from django.shortcuts import render
from blog.models import Post
from services.models import Service
#from django.http import HttpResponse


from .forms import PostForm

# Create your views here.

def index(request):

  recent_posts = Post.objects.order_by('-date')[:3] #.all()
  services = Service.objects.all()

  return render(request, 'main/index.html', {
    'page': 'index',
    'title': 'Главная страница',
    'hero': {
      'title': 'Открой свою судьбу через мудрость карт',
      'description': 'Твои ответы уже предначертаны звёздами — давай откроем их вместе!',
      'slides': ['1.png', '2.png', '3.png'],
    },
    'recent_posts': recent_posts,
    'services': services
  })
  #return HttpResponse("Hello, world. You're at the main index.")

def about(request):

  data = {
    'page': 'about',
    'title': 'О нас',
    'services': Service.objects.all()
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
    'title': 'Контакты',
    'services': Service.objects.all()
  })
