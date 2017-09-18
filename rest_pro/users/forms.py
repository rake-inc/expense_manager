from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        first_name = forms.CharField(max_length=32)
        last_name = forms.CharField(max_length=32)
        email = forms.EmailField(max_length=128)

        fields =['username','first_name','last_name','email','password1','password2']
