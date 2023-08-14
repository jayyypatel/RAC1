import imp
import re
from django.shortcuts import render, redirect
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
from developer_app.models import Profile_dev
from emp_app.models import Profile_client
from signup_user.models import CustomUser
from .forms import RegisterForm, Signup_gen,loginUser
from django.contrib.auth import authenticate , logout 
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.utils.safestring import mark_safe
#forgot password
from django.utils.safestring import mark_safe
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
# Create your views here.

def signup_gen(request):
    form = Signup_gen()

    if request.method == 'POST':
        form = Signup_gen(request.POST)
        if form.is_valid():
            user_choice = form.cleaned_data.get('user_choice')
            return redirect('signup_user:signup_developer', user_choice = user_choice)

    return render(request,'signup_user/signup.html' , {'form' : form})

def signup(request, user_choice):    #register view
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.user_type = user_choice
            form.save()
            return redirect('signup_user:login_user')
        else:
            messages.info(request,mark_safe('1. Email must be in format like tmp@gmail.com <br/>2. Password Contains at list 8 character, alphabets and specials'))
            return render(request,'signup_user/signup_developer.html', {'form' : form})
    return render(request,'signup_user/signup_developer.html', {'form' : form})

def login_user(request):  #login view
    form = loginUser()
    if request.method == 'POST':
        

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user is not None:
            auth_login(request,user)
            

            if request.user.user_type == 'developer':
                if Profile_dev.objects.filter(user_id_fk=request.user).exists():
                    return redirect('core:index')
                else:
                    return redirect('core:profile_pg')

            elif request.user.user_type == 'client':
                if Profile_client.objects.filter(user_id_fk=request.user).exists():
                    return redirect('core:index')
                else:
                    return redirect('core:profileemp_pg')
            elif request.user.user_type == 'ADMIN':
                print()
                print()
                print(' super ADMINNNNNNNNNNNNNNNNNNNNNNN ')
                return redirect('services:dashboard')
        else:
            messages.error(request,'Username or Password not correct')
            return render(request, 'signup_user/login.html', {'form' : form})

    return render(request, 'signup_user/login.html', {'form' : form})


def logout_user(request):
    logout(request)
    return redirect('signup_user:login_user')


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = CustomUser.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "signup_user/password_reset.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
                        
						send_mail(subject, email, settings.EMAIL_HOST_USER , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
                    
					return redirect("signup_user:password_reset_done")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="signup_user/password_reset.html", context={"password_reset_form":password_reset_form})