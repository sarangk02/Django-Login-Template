from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='signin')
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            my_user = User.objects.create_user(username, email, password)
            my_user.save()
            return redirect("signin")
        else:
            return HttpResponse("Passwords do not match")
    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        psw = request.POST.get('psw')
        res = authenticate(request, username=user, password=psw)
        print(user, psw, res)

        if res is not None:
            login(request, res)
            return redirect('home')
        else:
            return HttpResponse("Inavlid Credentials")
    return render(request, 'login.html')


def Logout(request):
    logout(request)
    return redirect('signin')
