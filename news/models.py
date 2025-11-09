import os
from django.db import models
from django.conf import settings
from blog.models import Country 




class NewsStory(models.Model):
	title = models.CharField(max_length=250, verbose_name='Заголовок')
	text = models.TextField(verbose_name='Текст новости')
	img = models.ImageField(upload_to='imgs/', null=True, blank=True, verbose_name = 'Фото в шапку страницы')
	country = models.ForeignKey(
		Country,
		on_delete=models.CASCADE,
		verbose_name='Страна'
	)
	published_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-published_at']
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'

	def __str__(self):
		return self.title
