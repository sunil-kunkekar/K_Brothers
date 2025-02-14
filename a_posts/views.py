from django.shortcuts import render

# Create your views here.
def home(request):
    title = 'Welcome To K_Brothers'
    return render(request, 'index.html',{'title':title})