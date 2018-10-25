from django_filters import rest_framework as filters
from rest_framework.viewsets import ViewSet, ModelViewSet, ReadOnlyModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from snippr.models.commit import Commit, Language, Snippet
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
                snippet = Snippet.objects.create(user=request.user, commit=commit, code=request.data['code'])  
                snippet = SnippetSerializer(snippet)
                retval = data.data
                retval['snippet'] = snippet.data
                retval['message'] = 'successfully created'
        return Response(retval)


class LanguageViews(ReadOnlyModelViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
