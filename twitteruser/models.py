from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Profile(AbstractUser):
    followers = models.ManyToManyField('self', blank=True, symmetrical=False)


def __str__(self):
    return self.username

