from django import forms
from expenses.models import Expense

class ExpenseForm(forms.ModelForm):
	class Meta():
		model = Expense
		fields = ['expense_type','expense_item','amount','create_date']

	def __init__(self, *args, **kwargs):
		super(ExerciseForm, self).__init__(*args, **kwargs)
		self.fields['expense_item'].required = False
		self.fields['amount'] = False