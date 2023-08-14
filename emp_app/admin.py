from django.contrib import admin

from emp_app.models import Profile_client, Project,Payment

# Register your models here.
admin.site.register(Profile_client)
admin.site.register(Project)
admin.site.register(Payment)