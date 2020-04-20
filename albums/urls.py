from django.urls import path
from albums import views


app_name='albums'

urlpatterns=[
	path('',views.AlbumListView.as_view(), name = 'index'),
	path('albumapi/',views.AlbumAPITemplateView.as_view(), name = 'albumapi'),

]