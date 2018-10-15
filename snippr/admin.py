from django.contrib import admin

from .models.userprofile import UserProfile
from .models.commit import Commit

admin.site.register(UserProfile)
admin.site.register(Commit)
