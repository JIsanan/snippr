from django.contrib import admin

from .models.userprofile import UserProfile

admin.site.register(UserProfile)
