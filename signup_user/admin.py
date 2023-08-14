from django.contrib import admin
from . import models
from signup_user.models import Address

admin.site.register(models.CustomUser)
admin.site.register(Address)