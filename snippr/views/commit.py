from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from snippr.models.commit import Commit
from snippr.serializers.user import UserSerializer
from snippr.serializers.commit import CommitSerializer


class CommitViews(ModelViewSet):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = Commit.objects.all()
	serializer_class = CommitSerializer

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
