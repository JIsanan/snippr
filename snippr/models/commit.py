from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


class Activity(models.Model):
    UPVOTE = 'U'
    ACTIVITY_TYPE = (
        (UPVOTE, 'upvote'),
    )

    user = models.ForeignKey(User,
                             related_name="likes",
                             on_delete=models.CASCADE
                             )
    is_active = models.BooleanField(default=True)
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPE)
    date = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


class Commit(models.Model):
    user = models.ForeignKey(
        User, related_name='commit', on_delete=models.CASCADE)
    language = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    title = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    lastest_update = models.DateTimeField(auto_now_add=True)
    upvote = GenericRelation(Activity)
