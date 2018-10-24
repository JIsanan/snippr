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


class Language(models.Model):
    name = models.CharField(max_length=20)


class Commit(models.Model):
    #for status field
    OPEN = 'O'
    CLOSED = 'C'
    STATUS_TAG = (
        (OPEN, 'Open'),
        (CLOSED, 'Closed')
    )

    user = models.ForeignKey(
        User, related_name='commits', on_delete=models.CASCADE)
    language = models.ForeignKey(Language, related_name='commits', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=240, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    latest_update = models.DateTimeField(auto_now_add=True)
    upvote = GenericRelation(Activity)
    status = models.CharField(max_length=1, default=OPEN, choices=STATUS_TAG)


class Snippet(models.Model):
    #for status field
    commit = models.ForeignKey(Commit, related_name='snippets', on_delete=models.CASCADE)
    code = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'date_created'