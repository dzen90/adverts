from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    last_visit = models.DateTimeField(null=True)
    avatar = models.ImageField(null=True, blank=True)
