from django import forms
from django.db.models import fields
from django.db.models.query import QuerySet
from django.forms import widgets
from core.models import Category
from emp_app.models import Project

class post_job_Form(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['project_title','project_description','project_duration','date','price_range','skill_choice','job_choice','category_id_fk']
        widgets = {
            'project_title' :forms.TextInput(attrs={'class':'form-control','placeholder':'Enter project title'}),
            'project_description' :forms.TextInput(attrs={'class':'form-control','placeholder':'Enter project description'}),
            'project_duration' :forms.TextInput(attrs={'class':'form-control','placeholder':'Enter project duration'}),
            'date' :forms.NumberInput(attrs={'class':'form-control','type':'date'}),
            'price_range' :forms.TextInput(attrs={'class':'form-control','placeholder':'Enter price range'}),
        
        }


class cate_post_job_Form(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['project_title','project_description','project_duration','date','price_range','skill_choice','job_choice']
        widgets = {
            'project_title' :forms.TextInput(attrs={'class':'form-control','placeholder':'Enter project title'}),
            'project_description' :forms.TextInput(attrs={'class':'form-control','placeholder':'Enter project description'}),
            'project_duration' :forms.TextInput(attrs={'class':'form-control','placeholder':'Enter project duration'}),
            'date' :forms.NumberInput(attrs={'class':'form-control','type':'date'}),
            'price_range' :forms.TextInput(attrs={'class':'form-control','placeholder':'Enter price range'}),
        
        }