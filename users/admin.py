from django.contrib import admin
from .models import CustomUser

# Register your models here.

admin.site.register(CustomUser)

AUTH_USER_MODEL = 'users.CustomUser'