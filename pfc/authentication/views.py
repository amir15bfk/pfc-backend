import imp
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import LoginSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib import auth
from django.conf import settings
import datetime
import timezone
import jwt
# Create your views here.



class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        short_password = True if len(request.data.get('password',''))<8 else False
        if serializer.is_valid() and not short_password:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        err = serializer.errors
        if short_password:
            if not err['password'] :
                err['password']=["Your password must be more then 8 characters"]
                
        return Response(err, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user:
            auth_token = jwt.encode(
                {'username': user.username,
                "exp": datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(days=3)},
                 settings.JWT_SECRET_KEY, algorithm="HS256")

            serializer = UserSerializer(user)

            data = {'user': serializer.data, 'token': auth_token}

            return Response(data, status=status.HTTP_200_OK)

            # SEND RES
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)