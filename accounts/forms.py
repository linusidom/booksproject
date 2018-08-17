from django import forms
from accounts.models import UserModel
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
	class Meta():
		model = UserModel
		fields = ['email','password1','password2',
				'ideal_carbs','ideal_protein','ideal_fat','ideal_weight','ideal_calories','current_weight']

class UserUpdateForm(forms.ModelForm):       
	class Meta:
		model = UserModel
		# Add all the fields you want a user to change
		fields = ['email','ideal_carbs','ideal_protein','ideal_fat','ideal_weight','ideal_calories','current_weight']

class InviteTrainerForm(forms.ModelForm):
	class Meta():
		model = UserModel
		fields = ['trainer_email']
