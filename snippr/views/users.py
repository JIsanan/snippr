from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.decorators import action
from rest_framework_simplejwt.views import TokenObtainPairView

from snippr.serializers import user
from django.contrib.auth.models import User


class UserViews(ViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = User.objects.all()
        serializer = user.UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user_obj = User.objects.filter(userprofile__id=pk).first()
        if(user_obj):
            serializer = user.UserSerializer(user_obj)
            return Response(serializer.data)
        return Response("User does not exist.")

    @action(detail=False)
    def my_profile(self, request):
        user_obj = request.user
        if(user_obj):
            serializer = user.UserSerializer(user_obj)
            return Response(serializer.data)
        return Response("User does not exist.")


class RegistrationViews(ViewSet):

    def create(self, request):
        obj = request.data
        x = user.RegisterSerializer(data=obj)
        res = {"message": "Please input correct credentials", }
        if x.is_valid() is True:
            new_user = x.save()
            res['message'] = "Successfully registered"
        return Response(res)


class LoginView(TokenObtainPairView):
    serializer_class = user.LoginSerializer
