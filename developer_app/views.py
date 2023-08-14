
from multiprocessing import context
from django.shortcuts import render,redirect
from developer_app.models import Profile_dev
from developer_app.forms import apply_now, profile_developer
from django.contrib.auth.decorators import login_required
from emp_app.models import Project
from services.models import Apply_project,Alloted_projects

from signup_user.models import CustomUser

# Create your views here.
def developer_index(request):
    freelancer = Profile_dev.objects.all()                            #this is for shows all profiles from database
    cnt = Profile_dev.objects.all().count()
    context = {
        'all_freelancer':freelancer,
        'count' : cnt      
    }
    return render(request,'developer_app/developer_index.html',context)

def browse_job(request):
    return render(request,'developer_app/browse_job.html')


@login_required(login_url='signup_user:login_user')

def apply_now_project(request,projectid):
    user = CustomUser.objects.get(pk=request.user.id)
    if user.user_type == 'client':
        return redirect('developer_app:apply_error')

    else:
    
        form = apply_now()

        if request.method == 'POST':
            form = apply_now(request.POST)
            

            if form.is_valid():
                form = form.save(commit=False)
                pro = Project.objects.get(id=projectid)
                form.applied_project_id_fk = pro
                form.applied_developer_id_fk = user
                form.save()
                return redirect('core:index')
    context = {'form':form}
      
    return render(request,'developer_app/applypg.html',context)


def apply_errorpg(request):
    return render(request,'developer_app/apply_error.html')


def applied_request(request):
    user = CustomUser.objects.get(pk=request.user.id)

    # devid = Profile_dev.objects.get(user_id_fk=user)
    pr_requst = Apply_project.objects.filter(applied_developer_id_fk=user,applied_status='False')
    context = {
        'pr_request' : pr_requst
    }

    return render(request,'developer_app/my_applied_request.html',context)

def alloted_projects(request):
    user = CustomUser.objects.get(pk=request.user.id)

    alloted_project = Alloted_projects.objects.filter(alloted_developer_id_fk=user)
    context ={
        'alloted_project' : alloted_project
    }
    return render(request,'developer_app/my_alloted_project.html',context)
 
def complete_project_st(request,alloteid):
    complete_obj = Alloted_projects.objects.get(id=alloteid)
    complete_obj.alloted_project_status = 'True'
    complete_obj.save()
    print(complete_obj.alloted_project_status)
    return redirect('developer_app:my_alloted_project')


def pr_dev_profile_pg(request,devid):
    profile_dev = Profile_dev.objects.get(id=devid)
    
    running_pro = Alloted_projects.objects.filter(alloted_developer_id_fk=profile_dev.user_id_fk,alloted_project_status='False')
    completed_pro = Alloted_projects.objects.filter(alloted_developer_id_fk=profile_dev.user_id_fk,alloted_project_status='True')
    
    context={
        'profile_dev' : profile_dev,
        'running_pro' : running_pro,
        'completed_pro' : completed_pro
    }
    return render(request,'developer_app/pr_dev_profile.html',context)

def myprofile_dev(request):
    user = CustomUser.objects.get(pk=request.user.id)
    profile = Profile_dev.objects.get(user_id_fk=user)
    running_pro = Alloted_projects.objects.filter(alloted_developer_id_fk=profile.user_id_fk,alloted_project_status='False')
    completed_pro = Alloted_projects.objects.filter(alloted_developer_id_fk=profile.user_id_fk,alloted_project_status='True')
    context={
        'profile' : profile,
        'running_pro' : running_pro,
        'completed_pro' : completed_pro
    }
    return render(request,'developer_app/myprofile_dev.html',context)
    