from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.welcome,name='home-page'),
    url(r'^search/',views.search_results, name='search_results'),
    url(r'^category/(\w+)', views.get_category,name='get_category'),
    url(r'^location/(\w+)', views.get_location,name='get_location'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  