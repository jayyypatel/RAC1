from django.db import models

from emp_app.models import Project
from signup_user.models import CustomUser
from django.utils import timezone


# Create your models here.

class Apply_project(models.Model):
   
    applied_price = models.IntegerField()
    applied_duration = models.CharField(max_length=10)
    applied_Date = models.DateTimeField(blank=True, null=True,default=timezone.now)
    applied_developer_id_fk = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='apllied_dev_developerid')
    applied_project_id_fk = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='applied_projectid')
    applied_status = models.BooleanField(default=False,blank=True,null=True)

    def __str__(self):
        return f'{self.applied_price} {self.applied_duration} {self.applied_Date}'

class Alloted_projects(models.Model):

    alloted_price = models.IntegerField(blank=True, null=True)
    alloted_duration = models.CharField(max_length=10,blank=True, null=True)
    alloted_Date = models.DateTimeField(blank=True, null=True,default=timezone.now)
    alloted_developer_id_fk = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='alloted_dev_developerid')
    alloted_project_id_fk = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='alloted_projectid')
    alloted_project_status = models.BooleanField(default=False,blank=True,null=True)
    razor_pay_order_id = models.CharField(max_length=1000,blank=True,null=True)
    paid = models.BooleanField(default=False,blank=True,null=True)

class Mailbox(models.Model):
    name = models.CharField(max_length = 150)
    email_id = models.EmailField(max_length=150)
    subject = models.CharField(max_length = 150)
    message = models.TextField()

class subscribe(models.Model):
    email = models.EmailField(max_length=150)
