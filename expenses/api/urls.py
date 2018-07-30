from django.conf.urls import url
from expenses.api import views

app_name = 'api_expenses'

urlpatterns = [
	url(r'(?P<pk>\d+)',views.ExpenseRUDAPIView.as_view(),name='api_expense'),
]
