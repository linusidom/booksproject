from django.conf.urls import url
from albums.api import views
app_name = 'api_albums'
urlpatterns = [
	url(r'^$', views.album_list, name = 'api_album_list'),
	url(r'(?P<pk>\d+)',views.album_detail,name='api_album_detail'),
]
