from django.conf.urls import url
from tagr.api import views
app_name = 'api_tagr'
urlpatterns = [
	url(r'(?P<pk>\d+)',views.PostRUDAPIView.as_view(),name='api_blog'),
]
