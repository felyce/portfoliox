from django.urls import path
from .views import signupfunc,Home
urlpatterns = [
    path('signup/',signupfunc,name='signup'),
    path('',Home.as_view(),name="home")
]
