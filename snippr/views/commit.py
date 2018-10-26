from django_filters import rest_framework as filters
from rest_framework.viewsets import ViewSet, ModelViewSet, ReadOnlyModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from snippr.models.commit import Commit, Language, Snippet, Activity
from snippr.serializers.user import UserSerializer
from snippr.serializers.commit import CommitSerializer, SnippetSerializer, LanguageSerializer


class CommitFilter(filters.FilterSet):
    language = filters.CharFilter(field_name='language__name')
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Commit
        fields = ['language', 'status', 'title']


class CommitViews(ModelViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Commit.objects.all()
    serializer_class = CommitSerializer
    filterset_class = CommitFilter

    def list(self, request):
        user = request.user.pk
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(
            queryset, many=True, context={'request': user})
        return Response(serializer.data)

    def create(self, request):
        language = Language.objects.filter(name=request.data['language']).first()
        retval = {}
        retval['message'] = 'something you inputted is wrong'
        if language and 'code' in request.data:
            obj = request.data.copy()
            obj['user'] = request.user.pk
            obj['language'] = language.pk
            data = CommitSerializer(data=obj)
            if data.is_valid() is True:
                commit = data.save()
                snippet = Snippet.objects.create(commit=commit, code=request.data['code'])  
                snippet = SnippetSerializer(snippet)
                retval = data.data
                retval['snippet'] = snippet.data
                retval['message'] = 'successfully created'
        return Response(retval)

    @action(detail=True, methods=['get'])
    def upvote(self, request, pk=None):
        user_obj = request.user
        commit = self.get_object()
        ret = {}
        ret['upvote_count'] = commit.upvote.filter(is_active=True).count()
        ret['upvote'] = True
        ret['downvote'] = False
        if(user_obj and commit):
            upvote = commit.upvote.filter(user=user_obj).first()
            if(upvote and not upvote.is_active):
                upvote.is_active = True
                upvote.save()
                ret['upvote_count'] += 1
            elif(not upvote):
                commit.upvote.create(
                    activity_type=Activity.UPVOTE, user=user_obj)
                ret['upvote_count'] += 1
        return Response(ret)

    @action(detail=True, methods=['get'])
    def downvote(self, request, pk=None):
        user_obj = request.user
        commit = self.get_object()
        ret = {}
        ret['upvote_count'] = commit.upvote.filter(is_active=True).count()
        ret['upvote'] = False
        ret['downvote'] = True
        if(user_obj and commit):
            upvote = commit.upvote.filter(user=user_obj).first()
            if(upvote and upvote.is_active):
                upvote.is_active = False
                upvote.save()
                ret['upvote_count'] -= 1
            elif(not upvote):
                commit.upvote.create(
                    activity_type=Activity.UPVOTE,
                    user=user_obj,
                    is_active=False)
                ret['upvote_count'] -= 1
        return Response(ret)


class LanguageViews(ReadOnlyModelViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
