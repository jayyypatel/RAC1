from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import widgets
from .models import Profile_dev
from services.models import Apply_project


class profile_developer(forms.ModelForm):

    class Meta:
        model = Profile_dev
        fields = ['your_skill','qualification','work_experience','past_project','job_type','location','salary','DOB','picture']
        widgets = {
                'your_skill' :forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your skills'}),
                'qualification' :forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your qualification'}),
                'work_experience' :forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your work_experience'}),
                'past_project' :forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your past_projects'}),
                'job_type' :forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your job_type'}),
                'location' :forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your location'}),
                'salary' :forms.TextInput(attrs={'class':'form-control','placeholder':'Enter expexted your salary'}),
                'DOB' :forms.NumberInput(attrs={'class':'form-control','type':'date'}),
                }

class apply_now(forms.ModelForm):

    class Meta:
        model = Apply_project
        fields = ['applied_price','applied_duration','applied_Date']
        widgets = {
            
            'applied_price' :forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your price'}),
            'applied_duration' :forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your duration'}),
            'applied_Date' :forms.NumberInput(attrs={'class':'form-control','type':'date'}),
        }