from django.shortcuts import render

# Create your views here.
def home(request):
    print("Hello")
    return render(request,'a_posts/home.html')