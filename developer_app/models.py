from datetime import datetime
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from signup_user.models import CustomUser 
from django.utils import timezone

# Create your models here.

class Profile_dev(models.Model):
    user_id_fk  = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='developer_userid')
    your_skill = models.CharField(max_length=100)
    qualification = models.CharField(max_length=10000)
    work_experience = models.CharField(max_length=10)
    past_project = models.CharField(max_length=100)   #worked in past company
    job_type = models.CharField(max_length=200)
    working_hours = models.CharField(max_length=100)
    location = models.CharField(max_length=10)
    salary= models.CharField(max_length=10)
    DOB = models.DateTimeField(blank=True, null=True,default=timezone.now)
    picture = models.ImageField(upload_to='Images',blank=True)
    
    def __str__(self):
        return f'{self.user_id_fk} {self.your_skill} {self.qualification} {self.work_experience} {self.past_project} {self.job_type} {self.working_hours} {self.location} {self.salary} {self.DOB}'

    def get_developer_image_url(self):
        return self.picture.url


class Work_dev(models.Model):
   
    Rent_per_hours = models.IntegerField()
    work_duration = models.CharField(max_length=10)
    Date = models.DateTimeField(blank=True, null=True,default=timezone.now)
    developer_id_fk = models.ForeignKey(Profile_dev,on_delete=models.CASCADE,related_name='Work_dev_developerid')

    def __str__(self):
        return f'{self.Rent_per_hours} {self.work_duration} {self.Date} {self.developer_id_fk}'
