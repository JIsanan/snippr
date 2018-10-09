from rest_framework.viewsets import ViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from snippr.serializers.user import UserSerializer
from django.contrib.auth import authenticate, login


class UserViews(ViewSet):
	authentication_classes = (TokenAuthentication,)
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
			x.save()
			res['message'] = "Successfully registered"
		return Response(res)

class LoginViews(ViewSet):

        def create(self, request):
                data = request.data
                username = data['username']
                password = data['password']
                resp = {}
                status_code = status.HTTP_200_OK

                user = authenticate(request, username=username, password=password)
                if user is not None:
                        login(request, user)
                        resp = {"status":"success","message":"Login Successful","status_code":status_code}
                else:
                        status_code = status.HTTP_401_UNAUTHORIZED
                        resp = {"status":"error","message":"Incorrect username and/or password","status_code":status_code}

                return Response(resp,status=status_code)

