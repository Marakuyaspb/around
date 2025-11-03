import os
from django.db import models
from django.conf import settings


class Category(models.Model):
	category_id = models.AutoField(primary_key=True)
	category = models.CharField(max_length=60, verbose_name='Категория')
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
	class Meta:
		ordering = ['country']
		indexes = [
			models.Index(fields=['country']),
		]
		verbose_name = 'Страна'
		verbose_name_plural = 'Страны'	

	def __str__(self):
		return self.country




class Place_name(models.Model):
	place_name_id = models.AutoField(primary_key=True)
	country = models.ForeignKey(Country,
		on_delete=models.CASCADE, verbose_name = 'Страна')
	place_name = models.CharField(max_length=60, verbose_name='Название места')
	class Meta:
		ordering = ['place_name']
		indexes = [
			models.Index(fields=['place_name']),
		]
		verbose_name = 'Место'
		verbose_name_plural = 'Места'	

	def __str__(self):
		return self.place_name





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
	place_name = models.ForeignKey(Place_name,
		on_delete=models.CASCADE, verbose_name = 'Название места')
	title = models.CharField(verbose_name ='Заголовок', max_length=200)
	text = models.TextField(verbose_name ='Текст статьи')
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
	def country(self):
		return self.place_name.country


	def __str__(self):
		return f'Статья "{self.title}"'


	def latest_3_articles(request):
		latest_articles = Article.objects.order_by('-updated_at')[:3]
		return render(request, 'latest_articles.html', {'_articles': _articles})

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