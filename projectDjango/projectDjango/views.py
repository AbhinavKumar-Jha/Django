from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world. You are at my Project's home page")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("Hello, world. You are at my Project's about page")

def contact(request):
    return HttpResponse("Hello, world. You are at my Project's contact page")