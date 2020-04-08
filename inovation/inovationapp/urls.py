from django.urls import path
from .views import signupfunc,Home,Ideas_list,opinion,main_list,goodfunc,branchfunc
urlpatterns = [
    path('signup/',signupfunc,name='signup'),
    path('',Home.as_view(),name="home"),
    path('ideas_list/',Ideas_list.as_view(),name="ideas_list"),
    path('opinion/<int:pk>',opinion,name="opinion"),
    path('main_list/<int:pk>',main_list,name="main_list"),
    path('good/<int:pk>',goodfunc,name="good"),
    path('branch/<int:pk>',branchfunc,name="branch")
]
