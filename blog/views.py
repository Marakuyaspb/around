import os
from django.shortcuts import render, get_object_or_404
from .models import *


def articles(request):
	articles = Article.objects.all
	context = {
		'articles':articles,
	}
	return render(request, 'blog/articles.html', context)


def the_article(request, id=None):
	if id:
		the_article = get_object_or_404(Article, article_id=id)

	articles = Article.objects.all

	context = {
		'the_article':the_article,
		'articles':articles,
	}
	return render(request, 'blog/the_article.html', context)