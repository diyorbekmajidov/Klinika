from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=False)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=100)



    def __str__(self):
        return self.first_name
