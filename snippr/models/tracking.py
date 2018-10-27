from .commit import Commit, Snippet, Activity

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation


class Tracking(models.Model):
    user = models.ForeignKey(
        User, related_name='comments', on_delete=models.CASCADE)
    commit = models.ForeignKey(Commit, related_name='comments', on_delete=models.CASCADE)
    snippet = models.ForeignKey(Snippet, related_name='comments', on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    upvote = GenericRelation(Activity)
    date_created = models.DateTimeField(auto_now_add=True)
    latest_update = models.DateTimeField(auto_now_add=True)
