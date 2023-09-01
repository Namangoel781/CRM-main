from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.contrib import messages
from .models import *
# Create your views here.

def login_view(request):

    if not request.user.is_authenticated:
        if request.method == 'POST':

            fm = UserLogin(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                userObj = authenticate(username=uname, password=upass)
                if userObj is not None:
                    login(request, userObj)
                    return HttpResponseRedirect('/home/')
        else:
            fm = UserLogin()
           

        return render(request, 'login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/home/')
    


def logout_view(request):
     
    logout(request)
     
    return HttpResponseRedirect('/')



def home(request):
    return render(request, 'home.html')

def register_user(request):
    return render(request, 'register.html')