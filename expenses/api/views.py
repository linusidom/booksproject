from rest_framework import generics
from expenses.api.models import ExpenseSerializer
from expenses.models import Expense

class ExpenseRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
	lookup ='pk'
	serializer_class = ExpenseSerializer
	queryset = Expense.objects.all()