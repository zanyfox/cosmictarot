from django.db import models

# Create your models here.

class Service(models.Model):
  name = models.CharField('Name', max_length=255)
  slug = models.CharField('Slug', max_length=255)
  excerpt = models.CharField('Excerpt', max_length=255, blank=True)
  body = models.TextField()
  icon = models.CharField('Icon', max_length=20)
  active = models.BooleanField('Active', default=True)
  
  def __str__(self):
    return self.name