from django.urls import path, include, reverse
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog/', views.articles, name = 'blog'),
    path('blog/<int:id>/', views.the_article, name='the_article'),
]