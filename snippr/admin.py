from django.contrib import admin

from .models.userprofile import UserProfile, Feedback
from .models.commit import Commit, Activity, Language, Snippet
from .models.tracking import Tracking


class SnippetAdmin(admin.ModelAdmin):
    list_display = ('commit', 'code')


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(UserProfile)
admin.site.register(Commit)
admin.site.register(Snippet, SnippetAdmin)
admin.site.register(Activity)
admin.site.register(Feedback)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Tracking)
