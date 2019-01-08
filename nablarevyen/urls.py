from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('', include(('apps.frontpage.urls', 'frontpage'))),
    path('nyheter/', include(('apps.articles.urls', 'articles'))),
    path('om-oss/', include(('apps.about.urls', 'about'))),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('filer/', include('filer.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
