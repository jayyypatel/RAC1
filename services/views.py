from datetime import datetime
from multiprocessing import context
from django.shortcuts import render
import random
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from emp_app.models import Project
from services.models import Alloted_projects
from services.utils import pdf
from signup_user.models import CustomUser
from xhtml2pdf import pisa
import os
from django.shortcuts import redirect
from django.conf import settings
from core.models import Category
from django.http import HttpResponse
from django.views.generic import View

from django.views.decorators.csrf import csrf_exempt
import razorpay
from django.template.loader import render_to_string
from .forms import MailForm, subscribeform
from django.core.mail import send_mail
from smtplib import SMTPAuthenticationError,SMTPException
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from weasyprint import HTML
from django.db.models import Count
import os
from django.conf import settings
from signup_user.models import CustomUser
from .models import Alloted_projects
# os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")

def dashboard(request):
    developers = CustomUser.objects.filter(user_type='developer')
    client = CustomUser.objects.filter(user_type='client')
    all = CustomUser.objects.all()
    running = Alloted_projects.objects.filter(alloted_project_status=False)
    completed = Alloted_projects.objects.filter(alloted_project_status=True)

    context={
        'dev_cnt':developers.count(),
        'cln_cnt':client.count(),
        'all':all.count() - 2,
        'running':running.count(),
        'completed':completed.count()
    }
    return render(request,'services/index.html',context)

def runningpro(request):
    running = Alloted_projects.objects.filter(alloted_project_status=False)
    msg = 'Running Projects'
    
    context={
                'running':running,
                'date':datetime.now(),
                'msg':msg
    }    

    return pdf(context,'services/runningpro.html')

def completedpro(request):
    running = Alloted_projects.objects.filter(alloted_project_status=True)
    msg = 'Completed Projects'
    
    context={
                'running':running,
                'date':datetime.now(),
                'msg':msg
    }    

    return pdf(context,'services/runningpro.html')

def runningpage(request):
    running = Alloted_projects.objects.filter(alloted_project_status=False)
    context = {
        'data':running
    }
    return render(request,'services/runningpage.html',context)

def completedpage(request):
    running = Alloted_projects.objects.filter(alloted_project_status=True)
    context = {
        'data':running
    }
    return render(request,'services/completedpage.html',context)

# Create your views here.
def services_index(request):
    Category_display = list(Category.objects.all())
    Category_display = random.sample(Category_display,4)
    context = {
        'category_display' : Category_display
    }
    return render(request,'services/services_index.html',context)

def about_us(request):
    return render(request,'services/about_us.html')

@login_required(login_url='signup_user:login_user')

def payment(request,id):
    obj = Alloted_projects.objects.get(pk=id)
    client = razorpay.Client(auth =("rzp_test_e3vquYBOpKb0x4" , "xk2Zu4Y8lpn7s4OLVUODPFmf"))
    payment = client.order.create({'amount':obj.alloted_price * 100, 'currency':'INR',
                            'payment_capture':'1' })
    
    obj.razor_pay_order_id = payment['id']
    obj.save()
    print(payment)
    print(client)
    return render(request, 'services/payment.html' ,{'payment':payment})

@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        order_id = ""
        for key , val in a.items():
            if key == "razorpay_order_id":
                order_id = val
                break
    
        pro = Alloted_projects.objects.filter(razor_pay_order_id = order_id).first()
        pro.paid = True
        pro.save()
        

    return render(request, "services/success.html")

def mail_function(request):
    form = MailForm()
    
    if request.method == "POST":
        form = MailForm(request.POST)
        if form.is_valid():
            
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            to_mail = form.cleaned_data.get('email_id')
            print(form)
            form.save()
            
            #reply as email to contected person
            try:
                send_mail('Your Query is recevied',
                        'Thank you for your response....',#message
                        settings.EMAIL_HOST_USER,
                        [to_mail],
                        fail_silently= False
                        )
            except SMTPAuthenticationError as e: 
                print(e)
            except SMTPException as e :
                print('There was error in sending error:  ' + e)
            
            try:
                send_mail(subject,
                        f'from: {to_mail} {message}',#message
                        settings.EMAIL_HOST_USER,
                        [settings.EMAIL_HOST_USER],
                        fail_silently= False
                        )
            except SMTPException as e :
                print('There was error in sending error:  ' + e)

            return redirect('services:thanks')
    context = {
        'form' : form
    }
    return render(request, "core/contact.html", context=context)

def thanks_function(request):
    return render(request, "services/thanks.html")

 
def view_all_order(request):
    details = Alloted_projects.objects.all()
    context = {
        'details' : details
    }
    return render(request, 'services/invoice.html', context=context)

download_path = os.path.join(settings.MEDIA_ROOT, 'report.pdf')

def genreport(request,id):
    alloted = Alloted_projects.objects.get(pk=id)

    context={
        'alloted':alloted
    }    

    # full_url = request.build_absolute_uri(reverse('orders'))
    template_render = render_to_string('services/invoice.html',context)
    html = HTML(string=template_render)
    html.write_pdf(target=download_path)

    fs = FileSystemStorage(settings.MEDIA_ROOT)
    with fs.open('report.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        return response
    return response




def topclient(request):

    top_five_clients = Project.objects.filter().values('client_id_fk__company_name','client_id_fk__user_id_fk__email').annotate(client_count=Count('client_id_fk__company_name')).order_by('-client_count',)[:5]
    msg = 'Top 5 Clients based on Projects'
    
    context={
                'top_5':top_five_clients,
                'date':datetime.now(),
                'msg':msg
    }    

    return pdf(context,'services/topclient.html')


def topdeveloper(request):
    top_five_devs = Alloted_projects.objects.filter().values('alloted_developer_id_fk__first_name','alloted_developer_id_fk__last_name','alloted_developer_id_fk__email').annotate(dev_count=Count('alloted_developer_id_fk')).order_by('-dev_count',)[:5]
    msg = 'Top Developers based on Alloted Projects'
    print(top_five_devs)
    context={
                'top_5':top_five_devs,
                'date':datetime.now(),
                'msg':msg
    }    

    return pdf(context,'services/topdeveloper.html')
    

def topcategory(request):
    top_five_cat = Project.objects.filter().values('category_id_fk__type').annotate(cat_count=Count('category_id_fk__type')).order_by('-cat_count',)[:5]
    msg = 'Top 5 Categories based on Posted Projects'
    
    cnt = [i for i in range(1,5)]
    context={
                'top_5':top_five_cat,
                'date':datetime.now(),
                'cnt':cnt,
                'msg':msg
    }    

    return pdf(context,'services/topcategory.html')



def pdf_all_project_client(request):
    user = CustomUser.objects.get(pk=request.user.id)
    all = Alloted_projects.objects.filter(alloted_project_id_fk__client_id_fk__user_id_fk=user)
    print(all)
    msg = 'All Alloted Project report'
    context={
                'top_5':all,
                'date':datetime.now(),
                'msg':msg
    } 
    return pdf(context,'services/all_project_client.html')

def pdf_all_project_developer(request):
    user = CustomUser.objects.get(pk=request.user.id)
    all = Alloted_projects.objects.filter(alloted_developer_id_fk=user)
    print(all)
    msg = 'All Received Project report'
    ms2 = user
    context={
                'top_5':all,
                'date':datetime.now(),
                'msg':msg,
                'ms2':ms2
    } 
    return pdf(context,'services/all_project_developer.html')