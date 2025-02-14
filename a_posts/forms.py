from django.forms import ModelForm
from django import forms
from a_posts.models import *


class PostCreateForm(ModelForm):
    class Meta:
        model = POST
        fields = '__all__'
        labels = {
            'body' : 'Caption',
            'tags' : 'Category'
        }
        widgets = {
            'body' : forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a caption ...', 'class': 'font1 text-4xl'}),
            'url' : forms.TextInput(attrs={'placeholder': 'Add url ...'}),
            'tags' : forms.CheckboxSelectMultiple(),
        }