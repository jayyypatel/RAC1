from django.shortcuts import redirect, render
from core.models import Category
from developer_app.forms import profile_developer
from emp_app.forms import profile_client_form
from emp_app.models import Profile_client, Project
from developer_app.models import Profile_dev
import random
from .forms import cate_post_job_Form, post_job_Form
from signup_user.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from services.forms import subscribeform
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.
def index(request):
    #This is for all employee profile
    client = Profile_client.objects.all()          #this for clients shows on index page    
    cnt = Profile_client.objects.all().count()      #for count of clients

    Category_display = list(Category.objects.all())
    Category_display = random.sample(Category_display,4)
    category_color_display = list(Category.objects.all())
    category_color_display = random.sample(category_color_display,8)

    form = subscribeform()
    
    if request.method == "POST":
        form = subscribeform(request.POST)
        if form.is_valid():
            to_mail = form.cleaned_data.get('email')
            form.save()
            
            #reply as email to contected person
            send_mail('You are successfully subscribed',
                    'Thank you for your response....',#message
                    settings.EMAIL_HOST_USER,
                    [to_mail],
                    fail_silently= False
                    )

    context = {
        'all_client':client,
        'count' : cnt ,
        'category_display' : Category_display,
        'category_color_display' : category_color_display,
        'form_e':form
    }
    return render(request,'core/index.html',context)



def contact(request):
    return render(request,'core/contact.html')

@login_required(login_url='signup_user:login_user')
def post_job(request):
    user = CustomUser.objects.get(pk=request.user.id)

    if user.user_type == 'developer':
        return redirect('core:error')

    else:
        form = post_job_Form()
        
        if request.method == 'POST':

            form = post_job_Form(request.POST)
            

            if form.is_valid():
                form = form.save(commit=False)
                
                u = Profile_client.objects.get(user_id_fk = user)
                form.client_id_fk = u
                form.save()
                return redirect('developer_app:browse_job')

        return render(request,'core/post_job.html',{'form' : form})   

def profile(request):
    form = profile_developer()

    if request.method == 'POST':
        user = CustomUser.objects.get(pk=request.user.id)
        form = profile_developer(request.POST,request.FILES)
        
        if form.is_valid():
            form = form.save(commit=False)
            form.user_id_fk = user
            form.save()    
            return redirect('core:index')
    return render(request,'core/profile.html',{'form' : form})  #profile.html

def job_list(request):
    return render(request,'core/job_list.html')  

def profileemp(request):
    form = profile_client_form()

    if request.method == 'POST':
        user = CustomUser.objects.get(pk=request.user.id)
        form = profile_client_form(request.POST,request.FILES)
        
        if form.is_valid():
            form = form.save(commit=False)
            form.user_id_fk = user
            form.save()    
            return redirect('core:index')
    
    return render(request,'core/profileemp.html',{'form' : form})        

def parti_category(requst,catid):

    cat = Project.objects.filter(category_id_fk=catid)
    cnt = Project.objects.filter(category_id_fk=catid).count()
    context = {
        'cat' : cat,
        'cnt' : cnt
    }
    return render(requst,'core/particular_cat.html',context)

def errorpg(request):
    return render(request,'core/error.html')

@login_required(login_url='signup_user:login_user')
def category_post_job_pg(request,catid_pjob):
    user = CustomUser.objects.get(pk=request.user.id)

    if user.user_type == 'developer':
        return redirect('core:error')

    else:
        form = cate_post_job_Form()
        
        if request.method == 'POST':

            form = cate_post_job_Form(request.POST)
            
            print('helloo')
            if form.is_valid():
                form = form.save(commit=False)
                
                u = Profile_client.objects.get(user_id_fk = user)
                form.client_id_fk = u
                print('hello')
                obj = Category.objects.get(id=catid_pjob)

                form.category_id_fk = obj
                print('hello1')
                form.save()
                return redirect('developer_app:browse_job')
    return render(request,'core/category_post_job.html',{'form': form})

def searchjobs(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        
        if not query:
            return render(request, 'core/index.html')
        else:
                

            lookups= Q(project_title__icontains=query) | Q(category_id_fk__type__icontains=query)

            results= Project.objects.filter(lookups).distinct()
        
            if  results.exists():

                context={'results': results,
                         'r_count':results.count()
                         }
                return render(request, 'core/search_jobs.html', context)
            else:
                return render(request,'core/searchnotfound.html')

    else:
        return render(request, 'core/index.html')

def searchcompany(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        if not query:
            return redirect('emp_app:emp_index')  
        else:
            
            lookups= Q(company_name__icontains=query)

            results= Profile_client.objects.filter(lookups).distinct()
        
            if  results.exists():
                p_project = Project.objects.all()  
                context={'results': results,
                        'p_pro':p_project,
                        'r_count':results.count()
                         }
                return render(request, 'core/search_company.html', context)
            else:
                return render(request,'core/searchnotfound.html')
        

    else:
        return render(request, 'emp_app/emp_index.html')


def searchfreelancer(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        if not query:
            return redirect('developer_app:developer_index')  
        else:
            
            lookups= Q(user_id_fk__first_name__icontains=query)

            results= Profile_dev.objects.filter(lookups).distinct()
        
            if  results.exists():
            
                context={'results': results,
                        'r_count':results.count()
                         }
                return render(request, 'core/search_freelancer.html', context)
            else:
                return render(request,'core/searchnotfound.html')
        

    else:
        return render(request, 'developer_app:developer_index')

