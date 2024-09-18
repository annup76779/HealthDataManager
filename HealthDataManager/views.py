from django.shortcuts import redirect


def index(request):
    return redirect("get_daily_details")