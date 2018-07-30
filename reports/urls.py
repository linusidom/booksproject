from django.conf.urls import url
from reports import views

app_name='reports'

urlpatterns=[
	url(r'^$',views.IndexTemplateView.as_view(), name = 'index'),
	url(r'^rep/$',views.report_list, name = 'report_list'),
	url(r'^create_new_entry/$',views.create_new_entry, name = 'create_new_entry'),

]