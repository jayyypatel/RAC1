from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

user_choice=(
        ('developer','developer'),
        ('client','client'),
        ('ADMIN','ADMIN')
           
    )
class CustomUser(AbstractUser):
    
    user_type = models.CharField(max_length=50, choices=user_choice,default='client')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
        # return f'{self.username}'

class Address(models.Model):
    country = models.CharField(max_length=70)
    city = models.CharField(max_length=35)

    state = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.country} {self.city} {self.state}'