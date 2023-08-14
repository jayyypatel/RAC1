from django.urls import path
from . import views
app_name = 'services'

urlpatterns = [
    path("services_index",views.services_index,name="services_index"),
    path("about_us",views.about_us,name="about_us"),
    # path('handlerequest/', views.handlerequest, name = 'handlerequest'),
    # path('pdf/',views.GenerateInvoice.as_view()),
    path("<int:id>/payment/",views.payment,name="payment"),
    path("success/",views.success,name="success"),
    path('mail/', views.mail_function, name='mail'),
    path('thanks/', views.thanks_function, name="thanks"),
    path("pdf/", views.view_all_order, name='orders'),
    path('<int:id>genreport/', views.genreport, name='genreport'),
    path("topclient/", views.topclient, name='topclient'),
    path("topdeveloper/", views.topdeveloper, name='topdeveloper'),
    path("topcategory/", views.topcategory, name='topcategory'),
    path("pdf_all_project_client/",views.pdf_all_project_client,name='pdf_all_project_client'),
    path("pdf_all_project_developer/",views.pdf_all_project_developer,name='pdf_all_project_developer'),
    path("dashboard/",views.dashboard,name='dashboard'),
    path("runningpro/", views.runningpro, name='runningpro'),
    path('completedpro/',views.completedpro,name='completedpro'),
    path('runningpage/',views.runningpage,name='runningpage'),
    path('completedpage/',views.completedpage,name='completedpage')
    ]