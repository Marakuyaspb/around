from django.urls import path, include, reverse
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog/', views.articles, name = 'blog'),
    # single article
    path('blog/<slug:slug>/',views.the_article, name='the_article'),
    
    path('search/', views.search, name='search'),


    # all articles in one category
    path('blog/<slug:category_slug>/', views.by_category, name='by_category'),

    # all articles in one country
    path('blog/<slug:country_slug>/', views.by_country, name='by_country'),

    # all articles in one region
    path('blog/<slug:country_slug>/<slug:region_slug>/', views.by_region, name='by_region'),

]