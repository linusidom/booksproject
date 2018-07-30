from django.conf.urls import url
from foods import views


app_name='foods'

urlpatterns=[
	url(r'^$',views.FoodListView.as_view(), name = 'food_list'),
	url(r'^(?P<pk>\d+)$',views.FoodDetailView.as_view(), name = 'food_detail'),
	url(r'^create/$',views.FoodCreateView.as_view(), name = 'food_create'),
	url(r'^(?P<pk>\d+)/update/$',views.FoodUpdateView.as_view(), name = 'food_update'),
	url(r'^(?P<pk>\d+)/delete/$',views.FoodDeleteView.as_view(), name = 'food_delete'),	
]