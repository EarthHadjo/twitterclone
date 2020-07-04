from django.shortcuts import render, reverse, HttpResponseRedirect
from twitteruser.models import TwitterUser
from authentication.forms import SignupForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet


@login_required
def index(request):
    info = settings.AUTH_USER_MODEL
    return render(request, 'index.html', {'info': info})


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = TwitterUser.objects.create_user(
                username=data['username'],
                display_name=data['display_name'],
                password=data['password1'],
            )
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
    form = SignupForm()
    return render(request, 'SignupForm.html', {'form': form})


@login_required
def profile_view(request, id):
    tweets = Tweet.objects.filter(author=id)
    counttweets = tweets.count()
    user = TwitterUser.objects.get(id=id)
    followers = user.followers.all()
    countfollowers = followers.count()
    if request.user.is_authenticated:
        myfollowers = request.user.followers.all()
        if user in myfollowers:
            is_following = True
        else:
            is_following = False
        return render(
                request,
                'authorinfo.html', {
                'tweets': tweets,
                'counttweets': counttweets,
                'user': user,
                'countfollowers': countfollowers,
                'myfollowers': myfollowers,
                'is_following': is_following,
                })
    return render(
                request,
                'authorinfo.html', {
                'tweets': tweets,
                'counttweets': counttweets,
                'user': user,
                'countfollowers': countfollowers,
                })


@login_required
def follow_view(request, id):
    user = request.user
    follow = TwitterUser.objects.get(id=id)
    user.followers.add(follow)
    user.save()
    return HttpResponseRedirect(reverse('authorinfo', args={id,}))


@login_required
def unfollow(request, id):
    user = request.user
    follow = TwitterUser.objects.get(id=id)
    user.followers.remove(follow)
    user.save()
    return HttpResponseRedirect(reverse('authorinfo', args={id,}))
