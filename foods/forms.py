from django import forms

from foods.models import Food
from expenses.models import Expense
from django.contrib.auth import get_user_model, get_user

User = get_user_model()

class FoodForm(forms.ModelForm):
	class Meta():
		model = Food
		fields = ['food_item','servings','calories','carbs','protein','fat','create_date']

	def __init__(self, *args, **kwargs):
		super(ExerciseForm, self).__init__(*args, **kwargs)
		self.fields['food_item'].required = False
		self.fields['servings'] = False
		self.fields['calories'] = False
		self.fields['carbs'] = False
		self.fields['protein'] = False
		self.fields['fat'] = False
		
		