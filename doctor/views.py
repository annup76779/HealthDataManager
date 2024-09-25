from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from shared.enums import UserType


# Create your views here.
@login_required
def home(request):
    if request.user.role != 'Doctor':
        logout(request)
        return redirect("login")
    return render(request, "doctor/home.html")
