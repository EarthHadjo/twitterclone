from django.shortcuts import render, reverse, HttpResponseRedirect
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from notification.models import Notification
from twitterclone.tweet.forms import TweetForm
from django.contrib.auth.decorators import login_required


@login_required()
def tweet_creation_view(request):
    html = "generic.html"
    header = "Welcome Friend!"
    form = None
    button_value = "Post your tweet!"

    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(
                user=request.user.twitteruser,
                tweet=data["tweet"],
            )
            user_matches = re.findall(r"@(\w+)", data["tweet"])
            for match in user_matches:
                Notification.objects.create(
                    username=TwitterUser.objects.filter(username=match).first(),
                    tweet=tweet
                )
        return HttpResponseRedirect(reverse("home"))
    else:
        form = TweetForm()
    return render(request, html, {"header": header, "form": form,
                                  "button_value": button_value})


def tweet_view(request, id):
    html = "tweets.html"
    tweets = Tweet.objects.filter(id=id)
    return render(request, html, {"tweets": tweets})
