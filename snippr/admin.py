from django.contrib import admin

from .models.userprofile import UserProfile
from .models.commit import Commit, Activity, Language, Snippet


class SnippetAdmin(admin.ModelAdmin):
    list_display = ('commit', 'code')


admin.site.register(UserProfile)
admin.site.register(Commit)
admin.site.register(Snippet, SnippetAdmin)
admin.site.register(Activity)
admin.site.register(Language)
