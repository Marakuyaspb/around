from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib import admin

from blog import views, urls
from main import views, urls
from news import views, urls



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('main.urls')),
    path('', include('news.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)