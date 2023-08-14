import datetime
from django.core.files.storage import default_storage
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from signup_user.models import CustomUser
from datetime import date, datetime
from django.utils import timezone
from core.models import Category
from developer_app.models import Profile_dev, Work_dev


# Create your models here.

class Profile_client(models.Model):
    user_id_fk  = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='client_userid')
    company_name = models.CharField(max_length=100)
    company_description = models.TextField(max_length=20000,blank=True)
    qualification = models.CharField(max_length=10000)
    NoOfEmployees = models.CharField(max_length=50,blank=True,null=True)
    Designation = models.CharField(max_length=100)
    amount_range = models.CharField(max_length=50)
    DOB = models.DateTimeField(blank=True, null=True,default=timezone.now)
    location = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='images',blank=True)
    
    def get_client_image_url(self):
        return f"{self.picture.url}"

    def __str__(self):
        return f'{self.user_id_fk}'


skill_type = (                          #first for id/db ,second for display 
    ('front-end','Front-end'),
    ('back-end','Back-end'),
    ('full-stack','Full-stack')
)
job_type = (
    ('fulltime','Full-time'),
    ('parttime','Part-time')
)
class Project(models.Model):
    project_title = models.CharField(max_length=100)
    project_description =models.TextField(max_length=20000,blank=True)
    project_duration = models.CharField(max_length=10,blank=True,null=True)
    date = models.DateTimeField(blank=True, null=True,default=timezone.now)
    price_range = models.CharField(max_length=10,blank=True,null=True)
    skill_choice =models.CharField(choices=skill_type,max_length=10,default='full-stack')
    job_choice = models.CharField(choices=job_type,max_length=10,default='Fulltime')
    client_id_fk = models.ForeignKey(Profile_client,on_delete=models.CASCADE,related_name='project_client')
    category_id_fk = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='project_category')
    project_status = models.BooleanField(default=False,blank=True,null=True)

    def __str__(self):
        return f'{self.id}'
    #     return f'{self.project_title} {self.project_description} {self.date} {self.price_range} {self.skill_choice} {self.job_choice} {self.category_id_fk} {self.category_id_fk}'

    def get_image_url_fk(self):
        return self.client_id_fk.picture.url

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    Rent_per_hours = models.DecimalField(max_digits=5, decimal_places=2)
    work_duration = models.IntegerField()
    client_id_fk = models.ForeignKey(Profile_client,on_delete=models.CASCADE,related_name='Payment_client')
    developer_id_fk = models.ForeignKey(Profile_dev,on_delete=models.CASCADE,related_name='Payment_developer')
    work_id_fk = models.ForeignKey(Work_dev,on_delete=models.CASCADE,related_name='payment_workid')


    def __str__(self):
        return f'{self.amount} {self.Rent_per_hours} {self.work_duration} {self.client_id_fk} {self.developer_id_fk} {self.work_id_fk}' 
