from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserModel(models.Model):
    Gender_Choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=7, choices=Gender_Choices)

    def __str__(self):
        return self.user.username
