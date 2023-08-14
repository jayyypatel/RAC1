from django import forms
from django.forms import widgets
from .models import Profile_client

class profile_client_form(forms.ModelForm):

    class Meta:
        model = Profile_client
        fields = ['company_name','company_description','qualification','NoOfEmployees','Designation','amount_range','DOB','location','picture']
        widgets = {
                'company_name' :forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your company name'}),
                'company_description' :forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your company_description'}),
                'qualification' :forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your qualification'}),
                'NoOfEmployees':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter noofemployees'}),
                'Designation' :forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your designation'}),
                'amount_range' :forms.TextInput(attrs={'class':'form-control','placeholder':'Enter range of amount'}),
                'DOB' :forms.NumberInput(attrs={'class':'form-control','type':'date'}),
                'location' :forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your location'})
                
                
                }