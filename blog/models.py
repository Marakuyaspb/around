import os
from django.db import models
from django.conf import settings
from markdownfield.models import MarkdownField, RenderedMarkdownField
from django.utils.text import slugify
from pytils.translit import slugify as translit_slug


class Category(models.Model):
	category_id = models.AutoField(primary_key=True)
	category = models.CharField(max_length=60, verbose_name='Категория')
	slug = models.SlugField(max_length=60, unique=True, blank=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			base = translit_slug(self.category)
			slug = base
			counter = 1
			while Category.objects.filter(slug=slug).exists():
				slug = f"{base}-{counter}"
				counter += 1
			self.slug = slug
		super().save(*args, **kwargs)


		
	class Meta:
		ordering = ['category']
		indexes = [
			models.Index(fields=['category']),
		]
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'	

	def __str__(self):
		return self.category




class Country(models.Model):
	country_id = models.AutoField(primary_key=True)
	country = models.CharField(max_length=60, verbose_name='Страна')
	slug = models.SlugField(max_length=60, unique=True, blank=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			base = translit_slug(self.country)
			slug = base
			counter = 1
			while Country.objects.filter(slug=slug).exists():
				slug = f"{base}-{counter}"
				counter += 1
			self.slug = slug
		super().save(*args, **kwargs)

	class Meta:
		ordering = ['country']
		indexes = [
			models.Index(fields=['country']),
		]
		verbose_name = 'Страна'
		verbose_name_plural = 'Страны'	

	def __str__(self):
		return self.country



class Region(models.Model):
	region_id = models.AutoField(primary_key=True)
	country = models.ForeignKey(Country,
		on_delete=models.CASCADE, verbose_name = 'Страна')
	region = models.CharField(max_length=60, verbose_name='Регион', default='Камчатка')
	slug = models.SlugField(max_length=60, unique=True, blank=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			base = translit_slug(self.region)
			slug = base
			counter = 1
			while Region.objects.filter(slug=slug).exists():
				slug = f"{base}-{counter}"
				counter += 1
			self.slug = slug
		super().save(*args, **kwargs)


	class Meta:
		ordering = ['region']
		indexes = [
			models.Index(fields=['region']),
		]
		verbose_name = 'Регион'
		verbose_name_plural = 'Регионы'	

	def __str__(self):
		return self.region


class Place_name(models.Model):
	place_name_id = models.AutoField(primary_key=True)
	region = models.ForeignKey(Region,
		on_delete=models.CASCADE, verbose_name = 'Регион')
	place_name = models.CharField(max_length=60, verbose_name='Название места', null=True, blank=True)
	place_name_source = models.CharField(max_length=60, verbose_name = 'Название места на языке страны', null=True, blank=True)

	class Meta:
		ordering = ['place_name']
		indexes = [
			models.Index(fields=['place_name']),
		]
		verbose_name = 'Место'
		verbose_name_plural = 'Места'	

	def __str__(self):
		return self.place_name

	@property
	def country(self):
		return self.region.country




class Tag(models.Model):
	id = models.AutoField(primary_key=True)
	tag = models.CharField(max_length=50, verbose_name='Ключевое слово', null=True, blank=True)

	class Meta:
		ordering = ['tag']
		indexes = [
			models.Index(fields=['tag']),
		]
		verbose_name = 'Ключевое слово'
		verbose_name_plural = 'Ключевые слова'

	def __str__(self):
		return self.tag




class Article(models.Model):
	article_id = models.AutoField(primary_key=True)
	category = models.ForeignKey(Category,
		on_delete=models.CASCADE, verbose_name = 'Категория')
	place_name = models.ForeignKey(Place_name, on_delete=models.CASCADE, verbose_name = 'Название места')
	title = models.CharField(verbose_name ='Заголовок', max_length=200)
	slug = models.SlugField(max_length=200, blank=True, unique=True, default='my-slugg')

	text = MarkdownField(rendered_field='text_html', verbose_name ='Текст статьи', null=True, blank=True)
	text_html = RenderedMarkdownField(null=True, blank=True)

	img_prev = models.ImageField(upload_to='imgs/', null=True, blank=True, verbose_name = 'Фото в шапку страницы')

	img_1 = models.ImageField(upload_to='imgs/', null=True, blank=True, verbose_name = 'Иллюстрация 1')
	img_2 = models.ImageField(upload_to='imgs/', null=True, blank=True, verbose_name = 'Иллюстрация 2')
	img_3 = models.ImageField(upload_to='imgs/', null=True, blank=True, verbose_name = 'Иллюстрация 3')
	img_4 = models.ImageField(upload_to='imgs/', null=True, blank=True, verbose_name = 'Иллюстрация 4')
	img_5 = models.ImageField(upload_to='imgs/', null=True, blank=True, verbose_name = 'Иллюстрация 5')
	img_6 = models.ImageField(upload_to='imgs/', null=True, blank=True, verbose_name = 'Иллюстрация 6')
	img_7 = models.ImageField(upload_to='imgs/', null=True, blank=True, verbose_name = 'Иллюстрация 7')
	img_8 = models.ImageField(upload_to='imgs/', null=True, blank=True, verbose_name = 'Иллюстрация 8')
	img_9 = models.ImageField(upload_to='imgs/', null=True, blank=True, verbose_name = 'Иллюстрация 9')
	img_10 = models.ImageField(upload_to='imgs/', null=True, blank=True, verbose_name = 'Иллюстрация 10')
	source = models.CharField(max_length=50, default='wikitravel')

	tags = models.ManyToManyField(Tag, related_name='articles', blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


	class Meta:
		ordering = ['title']
		indexes = [
			models.Index(fields=['title']),
		]
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'


	@property
	def place_name_source(self):
		return self.place_name.place_name_source

	@property
	def country_slug(self):
		return self.place_name.region.country.slug

	@property
	def region_slug(self):
		return self.place_name.region.slug

	@property
	def category_slug(self):
		return self.category.slug


	@property
	def country(self):
		return self.place_name.country.country

	@property
	def region(self):
		return self.place_name.region.region


	def __str__(self):
		return f'Статья "{self.title}"'


	def save(self, *args, **kwargs):
		if not self.slug:
			base = translit_slug(self.title)
			slug = base
			counter = 1
			while Article.objects.filter(slug=slug).exists():
				slug = f"{base}-{counter}"
				counter += 1
			self.slug = slug
		super().save(*args, **kwargs)


	def latest_3_articles(request):
		latest_articles = Article.objects.order_by('-updated_at')[:3]
		return render(request, 'latest_articles.html', {'latest_articles': latest_articles})

	def latest_10_articles(request):
		latest_articles = Article.objects.order_by('-updated_at')[:10]
		return render(request, 'latest_articles10.html', {'_articles10': _articles10})

	def first_sentence(self):
		sentences = self.text.split('. ')

		if len(sentences) > 1:
		    return '. '.join(sentences[:1]) + '.'
		elif sentences:
		    return sentences[0] + '.'
		return ''

	def first_two_sentences(self):
		sentences = self.text.split('. ')

		if len(sentences) > 1:
		    return '. '.join(sentences[:2]) + '.'
		elif sentences:
		    return sentences[0] + '.'
		return ''