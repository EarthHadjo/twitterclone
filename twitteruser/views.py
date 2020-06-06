from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from twitteruser.models import Profile
# from twitteruser.models import 
from notification.models import Notification
from twitteruser.models import Tweet


@login_required
def signup_view(request):
    html = "generic.html"
    header = "Signup"
    form = None
    button_value = "Signup"
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = Profile.objects.create_user(
                username=data["username"], password=data["password"])
            login_required(request, user)
            Profile.objects.create(
                username=data["username"],
                display_name=data["display_name"],
                user=user
            )
            return HttpResponseRedirect(redirect("home"))
    else:
        form = SignupForm()
    return render(request, html, {"header": header, "form": form,
                                  "button_value": button_value})


def profile_view(request, username):
    html = "twitteruser.html"
    targeteduser = Profile.objects.filter(username=username).first()
    targeteduser_tweets = Tweet.objects.filter(
        user=targeteduser).order_by("-date")
    num_tweets = len(targeteduser_tweets)
    num_followers = targeteduser.following.count()
    follow_status_button = None
    data = {}
    if request.user.is_authenticated:
        currentuser = Profile.objects.filter(
            username=request.user.twitteruser).first()
        notification = Notification.objects.filter(username=currentuser).count()
        if targeteduser not in currentuser.following.get_queryset():
            follow_status_button = "Follow"
        else:
            follow_status_button = "Unfollow"
        data = {"targeteduser": targeteduser, "tweets": targeteduser_tweets,
                "num_tweets": num_tweets,
                "follow_status_button": follow_status_button,
                "num_followers": num_followers,
                "notification": notification}
    else:
        data = {"targeteduser": targeteduser, "tweets": targeteduser_tweets,
                "num_tweets": num_tweets, "num_followers": num_followers}
    return render(request, html, data)

