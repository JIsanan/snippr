from rest_framework.viewsets import ViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import authenticate

from snippr.serializers.user import UserSerializer, LoginSerializer


class UserViews(ViewSet):
	# authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)

	def list(self, request):
		json = {"something": "hello"}
		return Response(json)


class RegistrationViews(ViewSet):

	def create(self, request):
		obj = request.data
		x = UserSerializer(data=obj)
		res = {"message": "Please input correct credentials",}
		if x.is_valid() is True:
			user = x.save()
			res['message'] = "Successfully registered"
		return Response(res)


class LoginViews(ViewSet):

	def create(self, request):
		obj = request.data
		user = authenticate(username=obj['username'], password=obj['password'])
		retval = {'message': 'incorrect'}
		if user is not None:
			retval = LoginSerializer(user)
			retval = retval.data
			retval['message'] = 'successful'
		return Response(retval)
