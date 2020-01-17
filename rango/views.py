from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hi, here is the link to the about page: <a href='/rango/about'>about</a>")

def about(request):
    return HttpResponse("This is the about page, here is the link to the index page: <a href='/rango/'>index</a>")
