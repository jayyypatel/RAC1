from django.urls import path
from . import views 

app_name = 'emp_app'

urlpatterns = [
    path("emp_index/",views.emp_index,name="emp_index"),
    path("temp_job/",views.temp_job,name="temp_job"),
    path("<int:clientid>/client_profile/",views.parti_client_profile,name='pr_client_profile'),
    path("project_request/",views.project_request_pg,name="project_request"),
    path("<int:projectid>/prti_project_request",views.prti_applied_project,name="prti_project_request"),
    path("<int:alloted_id>/allote_project",views.allote_project,name="allote_project"),
    path("alloted_project/",views.alloted_project,name="alloted_project_all"),
    path("myprofile_client/",views.myprofile_client,name="myprofile_client"),
    path("<int:p_id>/delete/",views.project_delete,name='delete_project'),
    
    ]