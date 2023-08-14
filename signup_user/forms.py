from django import forms
from django.forms import fields, widgets
# from django.forms.models import Labels
# from django.db.models import fields
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm


class RegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name' ,'email','password1', 'password2']
        widgets = {                                                       #it is used to add css and modify form 
            'username' :forms.TextInput(attrs={'class':'form-control'}),
            'first_name' :forms.TextInput(attrs={'class':'form-control'}),
            'last_name' :forms.TextInput(attrs={'class':'form-control'}),
            'email' :forms.TextInput(attrs={'class':'form-control'}),
            # 'password1' :forms.TextInput(attrs={'class':'form-control'}),
            # 'password2' :forms.TextInput(attrs={'class':'form-control'})
        }


class Signup_gen(forms.Form):
    USER_TYPE = (
        ('developer', "Developer"),
        ('client', 'Client'),
    )

    user_choice = forms.ChoiceField(choices=USER_TYPE, widget=forms.RadioSelect())
    
class loginUser(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}))
                                                           #it is used to add css and modify form 
