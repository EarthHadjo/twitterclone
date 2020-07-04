from django import forms
from twitteruser.models import TwitterUser


class UserForm(forms.ModelForm):
    class Meta:
        model = TwitterUser
        fields = ['username', 'password']


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.ModelForm):
    class Meta:
        model = TwitterUser
        fields = ['username', 'first_name',
                  'last_name', 'password', 'email']

