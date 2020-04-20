from django.urls import path, re_path
from reports import views

app_name='reports'

urlpatterns=[
	path('',views.IndexTemplateView.as_view(), name = 'index'),
	path('rep/',views.report_list, name = 'report_list'),
	path('create_new_entry/',views.create_new_entry, name = 'create_new_entry'),

]