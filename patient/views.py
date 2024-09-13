from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required
def add_daily_details(request):
    return render(request, "patient/add_daily_details.html")


@login_required
def get_daily_details(request):
    return render(request, "patient/daily_details_list.html")
