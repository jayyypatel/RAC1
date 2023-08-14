from email import message
from http import client
from multiprocessing import context
from django.shortcuts import redirect, render
from developer_app.models import Profile_dev
from emp_app.models import Profile_client, Project
from services.models import Alloted_projects, Apply_project
from signup_user.models import CustomUser

# from emp_app.models import Project

# Create your views here.
def emp_index(request):
    client = Profile_client.objects.all()              #This is for all employee profile
    cnt = Profile_client.objects.all().count()
    
    p_project = Project.objects.all()                   #this is for if condition used in emp_job_filter & used in client profile
    context = {
        'all_client':client,
        'count' : cnt ,
        'p_pro' : p_project
    }
    return render(request,'emp_app/emp_index.html',context)

def parti_client_profile(request,clientid):
    profile = Profile_client.objects.get(id=clientid)
    pr_project = Project.objects.filter(client_id_fk=clientid)
    context = {
        'pr_profile':profile,
        'pr_project':pr_project
    }
    return render(request,'emp_app/pr_profile.html',context)
def temp_job(request):
    # client = Profile_client.objects.all()
    # context = {
    #     'all_client':client      
    # }
    alloted_developer = Alloted_projects.objects.all()
    
    context ={
        'alloted_developer' : alloted_developer
    }
    return render(request,'emp_app/temp_job.html',context)


def project_request_pg(request):
    # context = { }
    
    user = CustomUser.objects.get(pk=request.user.id)

    clientid = Profile_client.objects.get(user_id_fk=user.id)

    pr_project = Project.objects.filter(client_id_fk=clientid)
    print(pr_project)
    
    context = {
        'pr_project':pr_project
    }
    return render(request,'emp_app/project_request.html',context)

def prti_applied_project(request,projectid):
    
    if Apply_project.objects.filter(applied_project_id_fk=projectid).exists():
        developer_request = Apply_project.objects.filter(applied_project_id_fk=projectid,applied_status='False')
        pic = []    
        for i in developer_request:
            pic.append(Profile_dev.objects.get(user_id_fk=i.applied_developer_id_fk))
        
        p = Project.objects.get(id=projectid)
        project_alloted = ''
        if Alloted_projects.objects.filter(alloted_project_id_fk=p).exists():
           project_alloted =  Alloted_projects.objects.get(alloted_project_id_fk=p)


           
        context ={

                    'developer_request' : developer_request,
                    'pic':pic,
                    'exists' : project_alloted
                    }
    else:
        context ={}

    return render(request,'emp_app/prti_project_request.html',context)


def allote_project(request,alloted_id):     # this is view for allote project with id , it calls after accept button clicks

    applied = Apply_project.objects.get(id=alloted_id)
    

    alot = Alloted_projects.objects.create(alloted_price=applied.applied_price,alloted_duration=applied.applied_duration,alloted_developer_id_fk=applied.applied_developer_id_fk,alloted_project_id_fk=applied.applied_project_id_fk)
    alot.save()

    
    applied_project =Apply_project.objects.get(id=alloted_id)
    app= Apply_project.objects.filter(applied_project_id_fk=applied_project.applied_project_id_fk)
    for i in app:
        i.applied_status = 'True'
        i.save()
    pro_obj = Project.objects.get(id=applied_project.applied_project_id_fk.id)
    pro_obj.project_status = 'True'
    pro_obj.save()
    
    if alot:
        return redirect('emp_app:alloted_project_all')
    return render(request,'emp_app/prti_project_request.html',context)
    

def alloted_project(request):               # this view is for alloted project without id for passing in url
    user = CustomUser.objects.get(pk=request.user.id)
    client = Profile_client.objects.get(user_id_fk=user)
    alloted_developer = Alloted_projects.objects.filter(alloted_project_id_fk__client_id_fk=client)
    pic = []
    for i in alloted_developer:
        pic.append(Profile_dev.objects.get(user_id_fk=i.alloted_developer_id_fk))
    
    context ={
        'alloted_developer' : alloted_developer,
        'pic' : pic
    }

    return render(request,'emp_app/alloted_project.html',context)


def myprofile_client(request):
    user = CustomUser.objects.get(pk=request.user.id)
    profile = Profile_client.objects.get(user_id_fk=user)
    
    context={
        'profile' : profile
    }
    return render(request,'emp_app/myprofile_client.html',context)

def project_delete(request,p_id):
    p_obj = Project.objects.get(id=p_id)
    p_obj.delete()
    return redirect('emp_app:project_request')

