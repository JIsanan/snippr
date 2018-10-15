from rest_framework import serializers
from rest_framework.authtoken.models import Token
from snippr.models.commit import Commit


class CommitSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    upvotes = serializers.SerializerMethodField()

    class Meta:
        model = Commit
        fields = (
            'pk',
            'user',
            'username',
            'language',
            'code',
            'date_created',
            'title',
            'upvotes')

    def get_username(self, obj):
        ret = obj.user.username
        return ret

    def get_upvotes(self, obj):
        ret = obj.upvote.count()
        return ret