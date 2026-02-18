from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer
# Create your views here.

class UserRegistrationView(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer
    
    def post(self, request:Request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "User registered successfully.",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserLoginView(generics.GenericAPIView):
    
    def post(self, request:Request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            response = {
                "message": "Login Successful",
                "token": user.auth_token.key
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response({"error":"Invalid email or password Incorrect"}, status=status.HTTP_401_UNAUTHORIZED)
    
    def get(self, request:Request):
        content = {
			"user":str(request.user),
		    "auth":str(request.auth),
        }
        return Response(content, status=status.HTTP_200_OK)