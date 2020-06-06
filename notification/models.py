from django.db import models
from twitterclone import TwitterUser


class Notification(models.Model):
    username = models.ForeignKey(
        TwitterUser, on_delete=models.CASCADE)
    tweet = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    was_viewed = models.BooleanField(default=False)

    def __str__(self):
        return "{self.username.username} tweeted: {self.tweet.tweet}"
