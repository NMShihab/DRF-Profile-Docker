from django.shortcuts import render
from django.http import JsonResponse, response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

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