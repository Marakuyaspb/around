import os
from django.db import models
from django.conf import settings
from markdownfield.models import MarkdownField, RenderedMarkdownField
from django.utils.text import slugify
from blog.models import Country, Tag


class Theme(models.Model):
	theme_id = models.AutoField(primary_key=True)
	theme = models.CharField(max_length=50, verbose_name='Тематика', default='Культура')
	slug = models.SlugField(max_length=60, unique=True, blank=True)
	
	def save(self, *args, **kwargs):
		if not self.slug:
			base = translit_slug(self.theme)
			slug = base
			counter = 1
			while Theme.objects.filter(slug=slug).exists():
				slug = f"{base}-{counter}"
				counter += 1
			self.slug = slug
		super().save(*args, **kwargs)

	class Meta:
		ordering = ['theme']
		indexes = [
			models.Index(fields=['theme']),
		]
		verbose_name = 'Тематика'
		verbose_name_plural = 'Тематики'	

	def __str__(self):
		return self.theme


class NewsStory(models.Model):
	newsstory_id = models.AutoField(primary_key=True)
	country = models.ForeignKey(
		Country,
		on_delete=models.CASCADE,
		verbose_name='Страна'
	)
	theme = models.ForeignKey(
		Theme,
		on_delete=models.CASCADE,
		verbose_name='Тематика',
		default='1'
	)
	title = models.CharField(max_length=250, verbose_name='Заголовок')
	text = MarkdownField(rendered_field='text_html', verbose_name ='Текст новости', null=True, blank=True)
	text_html = RenderedMarkdownField(null=True, blank=True)
	photo_prev = models.ImageField(upload_to='news_photos/', null=True, blank=True, verbose_name = 'Фото')
	photo_1 = models.ImageField(upload_to='news_photos/', null=True, blank=True, verbose_name = 'Фото')
	photo_2 = models.ImageField(upload_to='news_photos/', null=True, blank=True, verbose_name = 'Фото')
	photo_3 = models.ImageField(upload_to='news_photos/', null=True, blank=True, verbose_name = 'Фото')
	source = models.CharField(max_length=50, default='wikitravel')

	tags = models.ManyToManyField(Tag, related_name='newsstories', blank=True)
	slug = models.SlugField(max_length=200, unique=True, blank=True, default='my-slug')
	published_at = models.DateTimeField(auto_now_add=True)


	class Meta:
		ordering = ['-published_at']
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'

	def __str__(self):
		return self.title


	def save(self, *args, **kwargs):
		if not self.slug:
			base = translit_slug(self.title)
			slug = base
			counter = 1
			while NewsStory.objects.filter(slug=slug).exists():
				slug = f"{base}-{counter}"
				counter += 1
			self.slug = slug
		super().save(*args, **kwargs)


	def latest_6_news(request):
		latest_news = NewsStory.objects.order_by('-published_at')[:6]
		return render(request, 'latest_news.html', {'latest_news': latest_news})


	def first_sentence(self):
		sentences = self.text.split('. ')

		if len(sentences) > 1:
		    return '. '.join(sentences[:1]) + '.'
		elif sentences:
		    return sentences[0] + '.'
		return ''