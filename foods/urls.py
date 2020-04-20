from django.urls import path, re_path
from foods import views


app_name='foods'

urlpatterns=[
	path('',views.FoodListView.as_view(), name = 'food_list'),
	re_path('detail/(?P<pk>\d+)',views.FoodDetailView.as_view(), name = 'food_detail'),
	path('create/',views.FoodCreateView.as_view(), name = 'food_create'),
	re_path('update/(?P<pk>\d+)/',views.FoodUpdateView.as_view(), name = 'food_update'),
	re_path('delete/(?P<pk>\d+)/',views.FoodDeleteView.as_view(), name = 'food_delete'),	
]