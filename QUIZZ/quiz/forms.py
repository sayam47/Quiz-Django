from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import AuthUser

class SignUpForm(UserCreationForm):
	username = forms.CharField(label = "username")
	first_name = forms.CharField(label = "first_name")
	password = forms.CharField(label = "password")
	
	class Meta:
		model = AuthUser
		fields = ("username", "first_name", "password", )