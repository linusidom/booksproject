from django.conf.urls import url
from albums import views


app_name='albums'

urlpatterns=[
	url(r'^$',views.AlbumListView.as_view(), name = 'index'),
	url(r'^albumapi/$',views.AlbumAPITemplateView.as_view(), name = 'albumapi'),

]