from django.urls import path, include, reverse
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'news'

urlpatterns = [
    path('news/', views.news_list, name = 'news'),
    path('news/<int:id>/', views.the_newsstory, name='the_newsstory'),
]