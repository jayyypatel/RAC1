from mailbox import Mailbox
from django.contrib import admin
from .models import  Apply_project,Alloted_projects, Mailbox, subscribe

# Register your models here.
admin.site.register(Apply_project)
admin.site.register(Alloted_projects)
admin.site.register(Mailbox)
admin.site.register(subscribe)