from dataclasses import fields
from django import forms 
from .models import Mailbox,subscribe


class MailForm(forms.ModelForm):
    class Meta:
        model = Mailbox
        fields = ['name','email_id','subject','message']
        widgets = {
                'name':forms.TextInput(attrs={'class':'form-control underline','placeholder':'Enter your Name'}), 
                'email_id':forms.EmailInput(attrs={'class':'form-control underline','placeholder':'Enter your Email'}),
                'subject':forms.TextInput(attrs={'class':'form-control underline','placeholder':'Enter Subject'}), 
                'message':forms.Textarea(attrs={'class':'form-control underline','placeholder':'Enter message'}) 
        }

class subscribeform(forms.ModelForm):
    class Meta:
        model = subscribe
        fields = ['email']
        widgets = {
            'email' : forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your Email'})
        }