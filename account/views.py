from django.shortcuts import render


# Create your views here.
def signup_view(request):
    return render(request, 'account/signup.html')


def login_view(request):
    return render(request, 'account/login.html')

def home_view(request):
    return render(request, 'test.html')