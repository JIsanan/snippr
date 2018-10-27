from rest_framework import serializers
from snippr.models.commit import Commit, Snippet, Language
from snippr.models.tracking import Tracking
from snipprcomparison import snipprcomparison


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


class TrackingSerializer(serializers.ModelSerializer):
    upvotes = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    snippet_code = serializers.SerializerMethodField()
    line_changed = serializers.SerializerMethodField()

    class Meta:
        model = Tracking
        fields = (
            'pk',
            'code',
            'snippet',
            'date_created',
            'latest_update',
            'user',
            'commit',
            'description',
            'upvotes',
            'snippet_code',
            'line_changed',
            'user_id',
            'username',)
        extra_kwargs = {
            'user': {'write_only': True}
        }

    def get_upvotes(self, obj):
        ret = obj.upvote.count()
        return ret

    def get_username(self, obj):
        ret = obj.user.username
        return ret

    def get_user_id(self, obj):
        ret = obj.user.userprofile.id
        return ret

    def get_snippet_code(self, obj):
        ret = obj.snippet.code
        return ret

    def get_line_changed(self, obj):
        ret = snipprcomparison.get_lines_changed(obj.snippet.code, obj.code)
        return ret


class CommitSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    upvotes = serializers.SerializerMethodField()
    has_upvoted = serializers.SerializerMethodField()
    has_downvoted = serializers.SerializerMethodField()
    language_name = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    snippet = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    comments = TrackingSerializer(many=True)

    class Meta:
        model = Commit
        fields = (
            'pk',
            'status',
            'snippet',
            'comments',
            'user',
            'comments',
            'user_id',
            'username',
            'language_name',
            'language',
            'date_created',
            'title',
            'description',
            'upvotes',
            'has_upvoted',
            'has_downvoted')
        extra_kwargs = {
            'user': {'write_only': True}
        }

    def get_current_user(self):
        if(self.context):
            return self.context['request'].user
        return False

    def get_username(self, obj):
        ret = obj.user.username
        return ret

    def get_user_id(self, obj):
        ret = obj.user.userprofile.id
        return ret

    def get_comments(self, obj):
        obj = obj.comments.all()
        obj = TrackingSerializer(obj, many=True)
        ret = obj.data
        return ret

    def get_language_name(self, obj):
        ret = obj.language.name
        return ret

    def get_upvotes(self, obj):
        ret = obj.upvote.filter(is_active=True).count()
        return ret

    def get_has_upvoted(self, obj):
        user = self.get_current_user()
        ret = obj.upvote.filter(user=user).first()
        return True if (ret and ret.is_active) else False

    def get_has_downvoted(self, obj):
        user = self.get_current_user()
        ret = obj.upvote.filter(user=user).first()
        return True if (ret and not ret.is_active) else False

    def get_status(self, obj):
        ret = obj.get_status_display()
        return ret

    def get_snippet(self, obj):
        snippet = obj.snippets.latest()
        ret = SnippetSerializer(snippet).data
        return ret
