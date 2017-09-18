from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from .forms import SignupForm
# Create your views here.

def home(request):
    return render(request,'home.html',{})

def user_signup(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
    return render(request,'signup.html',{'form':form})

@login_required
def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
