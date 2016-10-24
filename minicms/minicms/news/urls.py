from django.conf.urls import patterns, include, url

from django.contrib import admin

from news import views
from DjangoUeditor import urls as DjangoUeditor_urls
urlpatterns = [
    url(r'^$', views.first_page),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),

]

# use Django server /media/ files
from django.conf import settings

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
