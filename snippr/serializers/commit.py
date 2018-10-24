from rest_framework import serializers
from snippr.models.commit import Commit, Snippet, Language


class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = (
            'pk', 'code', 'date_created',)

class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = (
            'pk', 'name')

class CommitSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    upvotes = serializers.SerializerMethodField()
    has_upvoted = serializers.SerializerMethodField()
    language_name = serializers.SerializerMethodField()

    class Meta:
        model = Commit
        fields = (
            'pk',
            'user',
            'user_id',
            'username',
            'language_name',
            'language',
            'date_created',
            'title',
            'description',
            'upvotes',
            'has_upvoted')
        extra_kwargs = {
            'user': {'write_only': True}
        }

    def get_username(self, obj):
        ret = obj.user.username
        return ret

    def get_user_id(self, obj):
        ret = obj.user.userprofile.id
        return ret

    def get_language_name(self, obj):
        ret = obj.language.name
        return ret

    def get_upvotes(self, obj):
        ret = obj.upvote.count()
        return ret

    def get_has_upvoted(self, obj):
        ret = False
        return ret
