import os
from django.shortcuts import render


def error_404_view(request, exception):
    return render(request, 'main/404.html', status=404)


def index(request):
    return render(request, 'main/index.html')
