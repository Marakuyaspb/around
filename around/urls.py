from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib import admin

from blog import views, urls
from main import views, urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('main.urls')),
]
