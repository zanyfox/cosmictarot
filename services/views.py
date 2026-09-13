from django.shortcuts import render

# Create your views here.

def services_index(request):
  return render(request, 'services/index.html', {
    'title': 'Услуги',
    'hero': {
      'title': 'Discover Your Destiny Through the Wisdom of the Cards',
      'description': 'Your Answers Are Written in the Stars – Let\'s Reveal Them!',
      'slides': ['1.png', '2.png', '3.png'],
    }
  })