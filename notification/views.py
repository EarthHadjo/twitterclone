from django.shortcuts import render, reverse, HttpResponseRedirect
from django.shortcuts import Notification
from twitteruser.models import TwitterUser
from django.contrib.auth.decorators import login_required



@login_required()
def notification(request):
    html = "notification.html"
    currentuser = TwitterUser.objects.filter(
        user=request.user).first()
    notifications = Notification.objects.filter(username=currentuser)
    for notice in notifications:
        notice.delete()
    return render(request, html, {"notification": notification})
