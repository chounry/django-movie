from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
	class Meta:
		model = Movie
		exclude = ['slug']
		widgets = {
			'caption':forms.Textarea(attrs={'cols': 10, 'rows': 10}),
		}
	