from django.forms import ModelForm, TextInput, EmailInput, Textarea
#from .models import Post

class PostForm(ModelForm):
  class Meta:
    #model = Post
    fields = ['name', 'email', 'subject', 'message'] #'__all__'

    widgets = {
      'name': TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Name'
      }),
      'email': EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Email'
      }),
      'subject': TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Subject'
      }),
      'message': Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Message',
        'rows': '5'
      }),
    }