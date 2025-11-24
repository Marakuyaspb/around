from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from .models import *



@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
	list_display = ['theme']


@admin.register(NewsStory)
class NewsStoryAdmin(admin.ModelAdmin):
	list_display = ['title', 'country']
	list_filter = ['title']