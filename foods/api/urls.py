from django.conf.urls import url
from foods.api import views

app_name = 'api_foods'

urlpatterns = [
	url(r'(?P<pk>\d+)',views.FoodRUDAPIView.as_view(),name='api_food'),
	]
