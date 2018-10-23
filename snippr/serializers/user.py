from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from snippr.models.userprofile import UserProfile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.six import text_type


class UserSerializer(serializers.HyperlinkedModelSerializer):
    issue_count = serializers.SerializerMethodField()
    id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'issue_count',
            'id'
        )

    def get_issue_count(self, obj):
        ret = obj.commits.count()
        return ret

    def get_id(self, obj):
        ret = obj.userprofile.id
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


class LoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super(TokenObtainPairSerializer, self).validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = text_type(refresh)
        data['access'] = text_type(refresh.access_token)
        serializer = UserSerializer(self.user)
        data['user'] = serializer.data

        return data
