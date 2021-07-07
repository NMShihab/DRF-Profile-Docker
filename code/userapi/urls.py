from django.urls import path
from .views import test_apiview,hello_world, MyTokenObtainPairView,getUserProfile,getAllProfile

urlpatterns = [
    path("test",test_apiview,name="testapi"),
    path("hello",hello_world,name="hello"),
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path("user/profile/",getUserProfile,name="userProfile"),
    path("users",getAllProfile,name="users"),

    
]