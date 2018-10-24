from django.contrib import admin

from .models.userprofile import UserProfile
from .models.commit import Commit, Activity, Language, Snippet


admin.site.register(UserProfile)
admin.site.register(Commit)
admin.site.register(Snippet)
admin.site.register(Activity)
admin.site.register(Language)
