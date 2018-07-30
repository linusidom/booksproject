from django.conf.urls import url
from exercises.api import views

app_name = 'api_exercises'

urlpatterns = [
	url(r'(?P<pk>\d+)',views.ExerciseRUDAPIView.as_view(),name='api_exercise'),
	]
