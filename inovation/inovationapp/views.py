from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
# Create your views here.

def signupfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        prefectures2 = request.POST['prefectures']
        works2 = request.POST['works']
       
       
        try:
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error':'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username2,'', password2)
            user.profile.prefectures = prefectures2 
            user.profile.works = works2 
            user.save()
            return redirect('../accounts/login')
    return render(request, 'signup.html')

class Home(TemplateView):
    template_name = "home.html"






    