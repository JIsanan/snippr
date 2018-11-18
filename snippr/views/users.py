from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
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

    def patch(self, request, pk=None):
        user_obj = request.user
        res = {"message": "Please input correct credentials", }
        if 'password' in request.data:
            res['message'] = "Successfully updated"
            request.user.set_password(request.data['password'])
            request.user.save()
            return Response(res)
        if(user_obj):
            serializer = user.UserSerializer(user_obj, data=request.data, partial=True)
            if(serializer.is_valid()):
                serializer.save()
                res['message'] = "Successfully updated"
            else:
                print(serializer.errors)
        return Response(res)

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
        if_exists = User.objects.filter(email=request.data['email']).first()
        res = {"message": "Please input correct credentials", }
        if if_exists:
            res['message'] = []
            res['message'].append('Email has already been taken')
            res['status'] = status.HTTP_400_BAD_REQUEST
            return Response(res)
        x = user.RegisterSerializer(data=obj)
        if x.is_valid() is True:
            x.save()
            res['message'] = "Successfully registered"
            res['status'] = status.HTTP_200_OK
        else:
            if(x.errors and x.errors['username']):
                res['message'] = x.errors['username']
                res['status'] = status.HTTP_400_BAD_REQUEST
        return Response(res)


class FeedbackViews(ViewSet):
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        obj = request.data.copy()
        obj['user'] = request.user.pk
        x = user.FeedbackSerializer(data=obj)
        res = {"message": "Please input correct stuff", }
        if x.is_valid() is True:
            x.save()
            res['message'] = "Successfully given feedback"

        return Response(res)


class LoginView(TokenObtainPairView):
    serializer_class = user.LoginSerializer
