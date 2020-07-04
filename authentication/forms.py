from django import forms
from twitteruser.models import TwitterUser


class UserForm(forms.ModelForm):
    class Meta:
        model = TwitterUser
        fields = ['username', 'password']


class LoginForm(forms.ModelForm):
    class Meta:
        model = TwitterUser
        fields = ['username', 'password']


class SignupForm(forms.ModelForm):
    class Meta:
        model = TwitterUser
        fields = ['username', 'first_name',
                  'last_name', 'password', 'email']
