from django import forms
from expenses.models import Expense

class ExpenseForm(forms.ModelForm):
	class Meta():
		model = Expense
		fields = ['expense_type','expense_type','amount','create_date']