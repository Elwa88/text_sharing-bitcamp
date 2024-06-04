from django.shortcuts import render,redirect
from .forms import Userform
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('register')
    else:
        form=UserCreationForm()
        return render(request,'user/register.html',{'form':form})

def user_login(request):
    if request.method == "POST":
        form = Userform(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                                username = data['username'],
                                password = data['password'],)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                return redirect('login')
        else:
            return redirect('login')
    else:
        form = Userform()
        return render(request,'user/login.html',{'form':form})
    
def user_logout(request):
    logout(request)
    return redirect('login')