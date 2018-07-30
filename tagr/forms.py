from django import forms

from tagr.models import Post

class PostForm(forms.ModelForm):
	class Meta():
		model = Post
		fields = ['question','message','create_date']