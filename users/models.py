from django.contrib.auth.models import User, AbstractUser
from django.db import models


# Create your models here.
class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=6, choices=[('Male', 'Male'), ('Female', 'Female')], blank=True)

    def __str__(self):
        return self.user.username
