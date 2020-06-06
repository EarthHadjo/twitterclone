from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Profile(AbstractUser):
    followers = models.ManyToManyField('self', blank=True, symmetrical=False)


def __str__(self):
    return self.username


# @property
# def followers(self):
#     return followers.objects.filter(follow_user=self.user).count()


# @property
# def following(self):
#     return followers.objects.filter(abstractuser=self.user).count()


# def save(self, force_insert=False, force_update=False, using=None,
#          update_fields=None):
#     super().save()


# class Follow(models.Model):
#     main_user = models.ForeignKey(TwitterUser, related_name='main_user', on_delete=models.CASCADE)
#     follow_user = models.ForeignKey(Main_user, related_name='follow_user', on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)