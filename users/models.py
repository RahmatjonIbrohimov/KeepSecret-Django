from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usermodel')
    img = models.ImageField(upload_to='profile_img/', default='https://www.instagram.com/p/C1AzlKiI0IW/', null=True, blank=True)
    fullname = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=6, choices=[('Male', 'Male'), ('Female', 'Female')], blank=True)

    def __str__(self):
        return self.user.username
