from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from snippr.models.userprofile import UserProfile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    issue_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'issue_count')

    def get_issue_count(self, obj):
        ret = obj.commits.count()
        return ret


class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        UserProfile.objects.create(user=user)
        return user
