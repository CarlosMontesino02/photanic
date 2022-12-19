from django import forms
from photanic_app.models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class DateInput(forms.DateInput):
	input_type = 'date'

class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username','password1','password2','email')
	
class UserEdit(UserChangeForm):
	class Meta:
		model = User
		fields = ('username','email','country', 'rank', 'birth_date')
		widgets = {'birth_date' : DateInput()}

	
class ArticuloForm(forms.ModelForm):
	error_css_class = 'error-field'
	required_css_class = 'required-field'
	text = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))
	class Meta:
		model =  Articulo
		fields = ('title', 'text', 'plant_art')
	
class ComentForm(forms.ModelForm):
	error_css_class = 'error-field'
	required_css_class = 'required-field'
	text = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))
	class Meta:
		model =  Comentario
		fields = ('photo', 'text',)
