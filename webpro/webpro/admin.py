from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
from profiles.models import User


# Register the User model if it's not already registered
if not admin.site.is_registered(User):
    admin.site.register(User, UserAdmin)