from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):

	first_name = forms.CharField(label = "", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Email Address'}))
	last_mame= forms.CharField(label = "", max_length=20,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}))
	email = forms.EmailField(label = "", max_length=20,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}))



	class Meta:
		model = User
		fields = ('username', 'first_name','last_mame','email','password1','password2')



	def __init__(self, *args, **kwargs):
		super(SignUpForm,self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Username'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class ="form-text text-muted small"><Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.</span>'



		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class ="form-text text-muted small"><li>Your Password can\'t be too similar to your other persobal information</li><li>Your password must contain at least 8 characters.</li><li>Your Password can\'t be a to commonly used password</li><li>Your password can\'t be entirely numeric.</li></ul>'


		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class ="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>