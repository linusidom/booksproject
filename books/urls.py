from django.urls import path
from books import views


app_name='books'

urlpatterns=[
	path('',views.BookListView.as_view(), name = 'index'),
	path('bookapi/',views.BookAPITemplateView.as_view(), name = 'bookapi'),

]