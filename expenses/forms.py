from django import forms
from expenses.models import Expense
from foods.models import Food
from django.contrib.auth import get_user_model

User = get_user_model()

class ExpenseForm(forms.ModelForm):
	# food = forms.ModelChoiceField(queryset=Food.objects.all())
	class Meta():
		model = Expense
		fields = ['expense_type','expense_item','amount','create_date']

