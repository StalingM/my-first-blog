
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^adminpop/', admin.site.urls),
    url(r'', include('blog.urls')),
]
