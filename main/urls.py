from django.urls import path, include, reverse
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name = 'index'),
]