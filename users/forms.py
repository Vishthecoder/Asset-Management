from django.contrib.auth.models import User
from django import forms 
from .models import UserRegistrationModel

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(
		label='Password', widget=forms.PasswordInput())
	re_password = forms.CharField(
		label='Confirm Password', widget=forms.PasswordInput())
	
	class Meta:
		model = User
		fields = ('username','first_name','last_name','email')

		def clean_password2(self):
			if self.cleaned_data['re_password'] != self.cleaned_data['password']:
				raise forms.ValidationError('Passwords don\'t match.')
			return self.cleaned_data['re_password']


class UserEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name','last_name','email')
