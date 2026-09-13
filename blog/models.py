from django.db import models

# Create your models here.

class Post(models.Model):
  title = models.CharField('Title', max_length=200)
  anons = models.CharField('Anons', max_length=255, blank=True)
  full_text = models.TextField()
  author = models.CharField('Author', max_length=100, default='Anonymous')
  date = models.DateTimeField('Date', auto_now_add=True)

  def __str__(self):
    return f'{self.title} | {self.author}'

  class Meta:
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'