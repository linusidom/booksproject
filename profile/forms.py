from django import forms
from profile.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from allauth.account.forms import SignupForm

# class UserForm(UserCreationForm):
# 	class Meta():
# 		model = Profile
# 		fields = ['email','password1','password2',
# 				'ideal_carbs','ideal_protein','ideal_fat','ideal_weight','ideal_calories','current_weight']

class ProfileForm(SignupForm):
    class Meta:
        model = Profile

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['ideal_carbs'] = forms.CharField(required=True, initial=200)
        self.fields['ideal_protein'] = forms.CharField(required=True, initial=200)
        self.fields['ideal_fat'] = forms.CharField(required=True, initial=200)
        self.fields['ideal_weight'] = forms.CharField(required=True, initial=200)
        self.fields['ideal_calories'] = forms.CharField(required=True, initial=200)
        self.fields['current_weight'] = forms.CharField(required=True, initial=200)
        self.fields['trainer_email'] = forms.EmailField(required=False)

    def save(self, request):
        user = super(ProfileForm, self).save(request)
        user.ideal_carbs = self.cleaned_data.pop('ideal_carbs')
        user.ideal_protein = self.cleaned_data.pop('ideal_protein')
        user.ideal_fat = self.cleaned_data.pop('ideal_fat')
        user.ideal_weight = self.cleaned_data.pop('ideal_weight')
        user.ideal_calories = self.cleaned_data.pop('ideal_calories')
        user.current_weight = self.cleaned_data.pop('current_weight')
        user.trainer_email = self.cleaned_data.pop('trainer_email')
        Profile.objects.get_or_create(user_id=user.id,
            ideal_calories=user.ideal_calories,
            ideal_carbs=user.ideal_carbs,
            ideal_fat=user.ideal_fat,
            ideal_weight=user.ideal_weight,
            ideal_protein=user.ideal_protein,
            current_weight=user.current_weight,
            trainer_email=user.email)
        return user


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['current_weight','ideal_weight','ideal_calories','ideal_carbs','ideal_protein','ideal_fat']


class InviteTrainerForm(forms.ModelForm):
	class Meta():
		model = Profile
		fields = ['trainer_email']

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Enter Your Email Address'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Enter Your Password'}))
