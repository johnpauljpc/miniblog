from django.conf import settings
from django.conf.urls.static import static
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from django.contrib import admin
from django.urls import path, include

'''from .sitemaps import CategorySitemap, PostSitemap
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .sitemaps import CategorySitemap, PostSitemap

from django.urls import path, include
'''
from .sitemaps import *

sitemaps = {'category':CategorySitemap, 'post':PostSitemap}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('blog/',include('blog.urls')),
    
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
'''
