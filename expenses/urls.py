from django.urls import path, re_path
from expenses import views


app_name='expenses'

urlpatterns=[
	path('',views.ExpenseListView.as_view(), name = 'index'),
	re_path('detail/(?P<pk>\d+)',views.ExpenseDetailView.as_view(), name = 'expense_detail'),
	path('create/',views.ExpenseCreateView.as_view(), name = 'expense_create'),
	re_path('update/(?P<pk>\d+)/',views.ExpenseUpdateView.as_view(), name = 'expense_update'),
	re_path('delete/(?P<pk>\d+)/',views.ExpenseDeleteView.as_view(), name = 'expense_delete'),
]