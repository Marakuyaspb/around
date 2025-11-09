import os
from django.db.models import Q
from django.core.paginator import Paginator
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



def search(request):
	q = request.GET.get('q', '').strip()
	if q:
	# something was typed
		# Postgres fast full-text (GIN index friendly)
		# articles = (
		# 	Article.objects
		# 	.annotate(
		# 		search=SearchVector(
		# 			'title',
		# 			'text',
		# 			'category__category',
		# 			'place_name__place_name',
		# 			'place_name__country__country',
		# 			'tags__tag'
		# 		)
		# 	)
		# 	.filter(search=q).distinct()
		# )

		# ----------  SQLite / MySQL fallback ----------
		articles = Article.objects.filter(
			Q(title__icontains=q) |
			Q(text__icontains=q) |
			Q(category__category__icontains=q) |
			Q(place_name__place_name__icontains=q) |
			Q(place_name__country__country__icontains=q) |
			Q(tags__tag__icontains=q)
		).distinct()
	else:
		articles = Article.objects.none()

	# optional pagination
	paginator = Paginator(articles, 15)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	return render(request, 'blog/search.html', {'page_obj': page_obj, 'query': q, 'count': paginator.count})