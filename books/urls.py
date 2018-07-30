from django.conf.urls import url
from books import views


app_name='books'

urlpatterns=[
	url(r'^$',views.BookListView.as_view(), name = 'index'),
	url(r'^bookapi/$',views.BookAPITemplateView.as_view(), name = 'bookapi'),

]