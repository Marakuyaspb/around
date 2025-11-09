from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['category_id', 'category']
	list_filter = ['category']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
	list_display = ['country_id', 'country']
	list_filter = ['country']

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
	list_display = ['region_id', 'region']
	list_filter = ['region']

@admin.register(Place_name)
class Place_nameAdmin(admin.ModelAdmin):
	list_display = ['place_name_id', 'place_name']
	list_filter = ['place_name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ['id', 'tag']
	list_filter = ['tag']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ['article_id', 'category', 'place_name', 'title']
	list_filter = ['title']