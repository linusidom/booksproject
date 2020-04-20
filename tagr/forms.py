from django import forms

from tagr.models import Post

class PostForm(forms.ModelForm):
	class Meta():
		model = Post
		fields = ['question','message','create_date']
		labels = {
			'message': 'Name',
		}

class PostUpdateForm(forms.ModelForm):
	class Meta():
		model = Post
		fields = ['message']
		labels = {
			'message': '',
		}
		widgets = {
			'message': forms.Textarea(
                attrs={'placeholder': 'Enter answer here'}),
		}