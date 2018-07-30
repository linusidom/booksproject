from django.conf.urls import url
from tagr import views


app_name='tagr'

urlpatterns=[
	url(r'^$',views.IndexTemplateView.as_view(), name = 'index'),
	url(r'^questions/$',views.PostListView.as_view(), name = 'post_list'),
	url(r'^(?P<chapter>\d+)/(?P<pk>\d+)/$',views.PostDetailView.as_view(), name = 'post_detail'),
	url(r'^update/(?P<chapter>\d+)/(?P<pk>\d+)/$',views.PostUpdateView.as_view(), name = 'post_update'),
]