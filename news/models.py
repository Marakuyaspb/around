import os
from django.db import models
from django.conf import settings
from blog.models import Country, Tag




class NewsStory(models.Model):
	newsstory_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=250, verbose_name='Заголовок')
	text = models.TextField(verbose_name='Текст новости')
	img = models.ImageField(upload_to='imgs/', null=True, blank=True, verbose_name = 'Фото')
	country = models.ForeignKey(
		Country,
		on_delete=models.CASCADE,
		verbose_name='Страна'
	)
	tags = models.ManyToManyField(Tag, related_name='newsstories', blank=True)
	published_at = models.DateTimeField(auto_now_add=True)


	class Meta:
		ordering = ['-published_at']
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'

	def __str__(self):
		return self.title


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
