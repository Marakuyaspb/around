import os
from django.urls import reverse
from django.shortcuts import render
from blog.models import *


def error_404_view(request, exception):
    return render(request, 'main/404.html', status=404)

def custom_500_view(request):
    return render(request, 'main/500.html', status=500)

def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'main/index.html', context)
