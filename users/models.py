from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usermodel')
    img = models.ImageField(upload_to='profile_img/', default='https://www.instagram.com/p/C1AzlKiI0IW/', null=True, blank=True)
    fullname = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=6, choices=[('Male', 'Male'), ('Female', 'Female')], blank=True)
    
    def clean(self):
        if not self.phone_number.isdigit():
            raise ValidationError(
                'Faqat raqam kiriting. Belgi va Harflar mumkin emas!',
                params={'phone_number': self.phone_number},
            )
        if len(self.phone_number) <= 6:
            raise ValidationError('Raqamlar yetarlicha emas! Kamida 6 ta Raqam kiriting!')
        
    def __str__(self):
        return self.user.username