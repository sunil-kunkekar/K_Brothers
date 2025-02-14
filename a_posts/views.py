from django.shortcuts import render
from a_posts.models import *
# Create your views here.
def home(request):
    posts = POST.objects.all()
    return render(request,'a_posts/home.html',{'posts':posts})