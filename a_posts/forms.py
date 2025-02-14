from django.forms import ModelForm
from django import forms
from a_posts.models import *
class PostCreateForm(ModelForm):
    class Meta:
        model = POST
        fields = ['url', 'body']
        labels = {
            'body' : 'Caption',
        }
        widgets = {
            'body' : forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a caption ...', 'class': 'font1 text-4xl'}),
            'url' : forms.TextInput(attrs={'placeholder': 'Add url ...'}),
        }