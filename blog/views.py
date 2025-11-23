import os
from django.db.models import Q
from django.core.paginator import Paginator
from django.utils.text import slugify
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import *




def articles(request):
	articles = Article.objects.all()
	categories = Category.objects.all()

	context = {
		'articles':articles,
		'categories':categories,
	}
	return render(request, 'blog/articles.html', context)


def by_category(request, category_slug):
	category = get_object_or_404(Category, slug=category_slug)
	context = {
		'articles': category.article_set.all(),
		'categories': Category.objects.all(),
		'current_category': category
	}
	return render(request, 'blog/articles.html', context)




def _reverse_slug(model, field: str, slug: str):
	for obj in model.objects.all():
		if slugify(getattr(obj, field)) == slug:
			return getattr(obj, field)
	return None 





def by_country(request, country_slug):
	country = get_object_or_404(Country, slug=country_slug)
	context = {
		'articles': Article.objects.filter(place_name__region__country=country),
		'categories': Category.objects.all(), 
		'current_country': country}
	return render(request, 'blog/articles.html', context)



def by_region(request, country_slug, region_slug):
	region = get_object_or_404(Region, 
		slug=region_slug,
		country__slug=country_slug)
	context = {'articles': Article.objects.filter(place_name__region=region), 'categories': Category.objects.all(), 'current_region': region}
	return render(request, 'blog/articles.html', context)





def the_article(request, country_slug, region_slug, slug):
	article = get_object_or_404(Article,
		slug=slug,
		place_name__region__slug=region_slug,
		place_name__region__country__slug=country_slug)
	return render(request, 'blog/the_article.html', {'article': article})





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
