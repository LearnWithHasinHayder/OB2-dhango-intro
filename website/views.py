from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('<h1>Hello, World!</h1>')
    return render(request,'home.html')

def about(request):
    return HttpResponse('This is About Page')

def contact(request):
    return HttpResponse('This is Contact Page')