from django.shortcuts import render
from django.http import JsonResponse, response
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import MyTokenObtainPairSerializer, UserSerializer,UserDataSerializer



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



@api_view(['GET'])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getAllProfile(request):
    users = User.objects.all()
    serializer = UserDataSerializer(users,many=True)
    return Response(serializer.data)


@api_view(['GET','POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data","data":response.data})


    return Response({"message": "Hello, world!"})

def test_apiview(request):
    data ={
        'name':"abc",
        'age':20
    }
    return JsonResponse(data)