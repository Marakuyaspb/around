from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['category']
	list_filter = ['category']
	readonly_fields = ('slug',)
	

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
	list_display = ['country']
	list_filter = ['country']
	readonly_fields = ('slug',)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
	list_display = ['region']
	list_filter = ['region']
	readonly_fields = ('slug',)


@admin.register(Place_name)
class Place_nameAdmin(admin.ModelAdmin):
	list_display = ['place_name']
	list_filter = ['place_name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ['tag']
	list_filter = ['tag']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ['category', 'place_name', 'title']
	list_filter = ['title']
	readonly_fields = ('slug',)