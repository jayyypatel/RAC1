from developer_app.models import Profile_dev
from emp_app.models import Profile_client, Project
from core.models import Category
import random

def project(request):
    project = Project.objects.filter(project_status='False')
    p_cnt = Project.objects.filter(project_status='False').count()
    print(project)
    return {'all_project':project,'project_count' : p_cnt}

def verticle_feature_members(request):
    verticle_feature_members = Profile_client.objects.all()[:7]
    
    return {'feature_members':verticle_feature_members}

def topcat(request):
    Category_display = list(Category.objects.all())
    Category_display = random.sample(Category_display,5)

    return {'topcat' : Category_display}

def topclient(request):
    topclient = list(Profile_client.objects.all())
    topclient = random.sample(topclient,5)

    return {'topclient' : topclient}

def topdev(request):
    topdev = list(Profile_dev.objects.all())
    topdev = random.sample(topdev,5)

    return {'topdev' : topdev}