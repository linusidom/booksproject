from django.conf.urls import url
from books.api import views
app_name = 'api_books'
urlpatterns = [
	url(r'^$', views.book_list, name = 'api_book_list'),
	url(r'(?P<pk>\d+)',views.book_detail,name='api_book_detail'),

]
