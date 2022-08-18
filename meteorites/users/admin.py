from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModel, ClientEcommerce


admin.site.register(UserModel, UserAdmin)
admin.site.register(ClientEcommerce)
