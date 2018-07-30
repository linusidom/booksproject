from django.conf.urls import url
from exercises import views


app_name='exercises'

urlpatterns=[
	url(r'^$',views.ExerciseListView.as_view(), name = 'exercise_list'),
	url(r'^(?P<pk>\d+)/$',views.ExerciseDetailView.as_view(), name = 'exercise_detail'),
	url(r'^create/$',views.ExerciseCreateView.as_view(), name = 'exercise_create'),
	url(r'^update/(?P<pk>\d+)/$',views.ExerciseUpdateView.as_view(), name = 'exercise_update'),
	url(r'^delete/(?P<pk>\d+)/$',views.ExerciseDeleteView.as_view(), name = 'exercise_delete'),

	# List Detail Create Update Delete

]