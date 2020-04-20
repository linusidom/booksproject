from django.urls import path, re_path
from exercises import views


app_name='exercises'

urlpatterns=[
	path('',views.ExerciseListView.as_view(), name = 'exercise_list'),
	re_path('(?P<pk>\d+)/',views.ExerciseDetailView.as_view(), name = 'exercise_detail'),
	path('create/',views.ExerciseCreateView.as_view(), name = 'exercise_create'),
	re_path('update/(?P<pk>\d+)/',views.ExerciseUpdateView.as_view(), name = 'exercise_update'),
	re_path('delete/(?P<pk>\d+)/',views.ExerciseDeleteView.as_view(), name = 'exercise_delete'),

	# List Detail Create Update Delete

]