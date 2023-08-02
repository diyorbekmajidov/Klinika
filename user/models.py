from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=100)
    password = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=100, unique=False, default="")

    def __str__(self):
        return self.first_name