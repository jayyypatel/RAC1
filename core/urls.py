import errno
from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path("",index,name="index"),
    path("contact/",contact,name="contact"),
    path("post_job/",post_job,name="post_job"),
    path("profile/",profile,name="profile_pg"),
    path("profileemp/",profileemp,name="profileemp_pg"),
    path("job_list/",job_list,name="job_list"),
    path("<int:catid>/particular_cat/",parti_category,name="particular_cat"),
    path("error/",errorpg,name="error"),
    path("<int:catid_pjob>/category_post_job/",category_post_job_pg,name="category_post_job"),
    path("searchjobs/",searchjobs,name="searchjobs"),
    path("search_company/",searchcompany,name="search_company"),
    path("search_freelancer/",searchfreelancer,name="search_freelancer"),
    ]