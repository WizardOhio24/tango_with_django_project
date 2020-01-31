from django.shortcuts import render

from django.http import HttpResponse

from rango.models import Category

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]

    content_dict = {
        'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!',
        'categories': category_list
        }
    return render(request, 'rango/index.html', context=content_dict)

def about(request):
    content_dict = {'name': 'Richard Menzies'}
    return render(request, 'rango/about.html', context = content_dict)
