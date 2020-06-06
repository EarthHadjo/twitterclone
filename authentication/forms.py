from django import forms
from twitteruser.models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'password']
