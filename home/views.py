# import http
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    # return render(request, 'home.html', {"hello world"})
    # return HttpResponse("Hello, world k xa")
    context={'name':'sagar','subject':'python'}
    return render(request, 'home.html' , context)

def about(request):
    # return render(request, 'home.html', {"hello world"})
    return HttpResponse("Hello, world. You're at the About page.(/a)")
def contact(request):
    # return render(request, 'home.html', {"hello world"})
    return HttpResponse("Hello, world. You're at the Contact page.(/a)")
def project(request):
    # return render(request, 'home.html', {"hello world"})
    return HttpResponse("Hello, world. You're at the project page.(/a)")
