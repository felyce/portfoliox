from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, TemplateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Idea_list,Opinion,Profile
from django.db.models import Q
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

class Ideas_list(LoginRequiredMixin, ListView):
    template_name = 'ideas_list.html'
    model =  Idea_list
    def get_queryset(self):
        q_word = self.request.GET.get('query')

        if q_word:
            object_list = Idea_list.objects.filter(
                Q(genre__icontains=q_word))
        else:
            object_list = Idea_list.objects.all()
        return object_list

@login_required
def opinion(request,pk):
    idea = Idea_list.objects.get(pk=pk).genre
    if request.method == "POST":
        author2 = request.POST['author']
        title2 = request.POST['title']
        content2 = request.POST['content']
        Opinion.objects.create(author = author2,title=title2,content = content2,idea_list_id = pk)
        return redirect('main_list',pk=pk)
    return render(request, 'opinion.html',{'object':idea})

@login_required
def main_list(request,pk):
    d = {
        'main_idea':Opinion.objects.filter(idea_list_id=pk)
    }
    return render(request,"main_list.html",d)

@login_required        
def goodfunc(request, pk):
    post =  Opinion.objects.get(pk=pk)
    pk2 = post.idea_list_id
    post2 = request.user.get_username()
    if post2 in post.goodcheck:
        return redirect('main_list',pk=pk2)
    else:
        post.good += 1
        post.goodcheck = post.goodcheck + ' ' + post2
        post.save()
        return redirect('main_list',pk=pk2)

@login_required
def branchfunc(request, pk):
    user = request.user.get_username()
    post = Opinion.objects.filter(idea_list_id=pk).filter(author=user)
    if not post:
        return redirect('opinion',pk=pk)
    else:
        return redirect('main_list',pk=pk)

@login_required
def detailfunc(request,author):
    key = User.objects.get(username=author).id
    profile2 = Profile.objects.get(user_id=key)
    return render(request,'detail.html',{'profile':profile2})











    