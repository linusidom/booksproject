from django.urls import path, re_path
from reports import views

app_name='reports'

urlpatterns=[
	path('', views.report_list, name='index'),

]