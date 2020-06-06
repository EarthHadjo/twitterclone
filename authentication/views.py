from django.shortcuts import render, redirect
from twitteruser.models import Profile
from .forms import UserForm
from django.contrib.auth.decorators import login_required
# Create your views here.


