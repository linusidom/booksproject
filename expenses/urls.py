from django.conf.urls import url
from expenses import views


app_name='expenses'

urlpatterns=[
	url(r'^$',views.ExpenseListView.as_view(), name = 'expense_list'),
	url(r'^(?P<pk>\d+)$',views.ExpenseDetailView.as_view(), name = 'expense_detail'),
	url(r'^create/$',views.ExpenseCreateView.as_view(), name = 'expense_create'),
	# url(r'^create/$',views.expense_create, name = 'expense_create'),
	
	url(r'^(?P<pk>\d+)/update/$',views.ExpenseUpdateView.as_view(), name = 'expense_update'),
	
	url(r'^(?P<pk>\d+)/delete/$',views.ExpenseDeleteView.as_view(), name = 'expense_delete'),
]