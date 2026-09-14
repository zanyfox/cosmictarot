from django.shortcuts import render, get_object_or_404

from .models import Service

# Create your views here.

def services_index(request):

  services = Service.objects.all()
  
  return render(request, 'services/index.html', {
    'title': 'Услуги',
    'page': 'services',
    'services': services
  })

def service_detail(request, slug):
  service = get_object_or_404(Service, slug=slug)
  services = Service.objects.all()
  return render(request, 'services/detail.html', {
    'title': 'Услуги',
    'page': 'services',
    'service': service,
    'services': services
  })