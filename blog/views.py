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





def by_country(request, country_slug: str):
	country = get_object_or_404(Country, slug=country_slug)

	# статьи, относящиеся к этой стране
	articles = Article.objects.filter(country=country).select_related('region')

	# список всех стран (кроме текущей, чтобы не показывать её повторно)
	countries = Country.objects.exclude(country_id=country.country_id)

	return render(request, 'blog/articles_by_country.html', {
		'country': country.country,
		'articles': articles,
		'regions': Region.objects.filter(country=country),
		'countries': countries,
	})


def by_region(request, country_slug: str, region_slug: str):
	country = get_object_or_404(Country, slug=country_slug)
	region  = get_object_or_404(Region, country=country, slug=region_slug)

	# статьи конкретного региона
	articles = Article.objects.filter(region=region)

	# список всех стран (кроме страны, к которой относится этот регион)
	countries = Country.objects.exclude(country_id=country.country_id)

	return render(request, 'blog/articles_by_region.html', {
		'region': region,
		'articles': articles,
		'countries': countries,
	})




def the_article(request, slug: str):
	article = get_object_or_404(
	Article.objects
	.select_related(
		'category',                 # Category
		'place_name',               # Place_name
		'place_name__region',       # Region
		'place_name__region__country',  # Country
	),
	slug=slug
    )

	# готовые строки для шаблона (не дергаем property в цикле)
	country_slug = article.place_name.region.country.slug
	region_slug  = article.place_name.region.slug
	category_slug = article.category.slug

	return render(
		request,
		'blog/the_article.html',
		{
			'article': article,
			'country_slug': country_slug,
			'region_slug': region_slug,
			'category_slug': category_slug,
		}
	)





def search(request):
	q = request.GET.get('q', '').strip()
	if q:
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
