from django import forms
from photanic_app.models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username','password1','password2','email','country', 'rank', 'birth_date')
	
class UserEdit(UserChangeForm):
	class Meta:
		model = User
		fields = ('username','email','country', 'rank', 'birth_date')