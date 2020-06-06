from django.db import models
from tweet.models import Profile
from django.utils import timezone


class Tweet(models.Model):
    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE)
    tweet = models.CharField(max_length=140)
    date = models.DateTimeField(default=timezone.now)
