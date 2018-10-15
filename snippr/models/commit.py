from django.db import models
from django.contrib.auth.models import User


class Commit(models.Model):
    user = models.ForeignKey(
        User, related_name='commit', on_delete=models.CASCADE)
    language = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
