from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


# Create your views here.
def logout(request):
    auth_logout(request)
    return redirect('/board/list')


def login(request):
    if request.method == "GET":
        loginForm = AuthenticationForm()
        return render(request, 'user/login.html', {'loginForm': loginForm})
    elif request.method == "POST":
        loginForm = AuthenticationForm(request, request.POST)
        if loginForm.is_valid():
            auth_login(request, loginForm.get_user())
            return redirect('/board/list')
        # else:
        #     return redirect('/reply/list')


def signup(request):
    if request.method == "GET":
        signupForm = UserCreationForm()
        return render(request, 'user/signup.html', {'signupForm': signupForm})
    elif request.method == "POST":
        signupForm = UserCreationForm(request.POST)
        if signupForm.is_valid():
            user = signupForm.save(commit=False)
            user.save()
        return redirect('/board/list')

#def kakaoLogin(request):
#    return render(request, 'kakaologin.html')

@login_required(login_url='/user/login')
def myProfile(request):
    #username= request.user
    return render(request, 'myProfile.html')


def userDelete(request):
    user = request.user

    user.delete()
    logout(request)
    return render(request, 'user/delete_success.html',{})
