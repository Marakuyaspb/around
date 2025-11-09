from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from .models import *


@admin.register(NewsStory)
class NewsStoryAdmin(admin.ModelAdmin):
	list_display = ['newsstory_id', 'title', 'country']
	list_filter = ['title']