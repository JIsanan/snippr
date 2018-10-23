from django_filters import rest_framework as filters
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from snippr.models.commit import Commit
from snippr.serializers.user import UserSerializer
from snippr.serializers.commit import CommitSerializer


class CommitFilter(filters.FilterSet):
    language = filters.CharFilter(field_name='language__name')

    class Meta:
        model = Commit
        fields = ['language']


class CommitViews(ModelViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Commit.objects.all()
    serializer_class = CommitSerializer
    filterset_class = CommitFilter


    def create(self, request):
        obj = request.data.copy()
        obj['user'] = request.user.pk
        data = CommitSerializer(data=obj)
        retval = {}
        retval['message'] = 'something you inputted is wrong'
        if data.is_valid() is True:
            data.save()
            retval = data.data
            retval['message'] = 'successfully created'
        print(data.errors)
        return Response(retval)
