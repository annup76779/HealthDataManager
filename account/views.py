from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
def signup_view(request):
    return render(request, 'account/signup.html')


def login_view(request):
    return render(request, 'account/login.html')


def home_view(request):
    return render(request, 'test.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")
