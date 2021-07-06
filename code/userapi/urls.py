from django.urls import path
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView
    
# )
from .views import test_apiview,hello_world, MyTokenObtainPairView
urlpatterns = [
    path("test",test_apiview,name="testapi"),
    path("hello",hello_world,name="hello"),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair')

    
]