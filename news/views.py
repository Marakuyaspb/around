from django.shortcuts import render, get_object_or_404
from .models import NewsStory


def news_list(request):
    news_list = NewsStory.objects.all()
    context = {'news_list': news_list}
    return render(request, 'news/news_list.html', context)


def the_newsstory(request, id):
    """Одна новость (аналог blog/the_article)."""
    story = get_object_or_404(NewsStory, pk=id)
    context = {'story': story}
    return render(request, 'news/the_newsstory.html', context)