from django.urls import path
from . import views 

app_name = 'developer_app'

urlpatterns = [
    
    path("developer_index/",views.developer_index,name="developer_index"),
    path("browse_job/",views.browse_job,name="browse_job"),
    path("<int:projectid>/applypg/",views.apply_now_project,name="applypg"),
    path("apply_error/",views.apply_errorpg,name="apply_error"),
    path("my_applied_request/",views.applied_request,name="my_applied_request"),
    path("my_alloted_project/",views.alloted_projects,name="my_alloted_project"),
    path("<int:alloteid>/complete_project/",views.complete_project_st,name="complete_project"),
    path("<int:devid>/pr_dev_profile/",views.pr_dev_profile_pg,name="pr_dev_profile"),
    path("myprofile/",views.myprofile_dev,name="myprofile_dev")
    ]