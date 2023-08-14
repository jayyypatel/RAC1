from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'signup_user'

urlpatterns = [
    
    path("signup_gen/",views.signup_gen,name="signup_gen"),
    path("<str:user_choice>/signup_developer/",views.signup,name="signup_developer"),
    path("login_user/",views.login_user,name="login_user"),
    path("logout_user/",views.logout_user,name="logout_user"),
    


    #forgot password
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='signup_user/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="signup_user/password_reset_confirm.html",success_url="/signup_user/login_user/"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='signup_user/password_reset_complete.html'), name='password_reset_complete'), 

    path("password_reset", views.password_reset_request, name="password_reset")



    ]