from django.urls import path

from account.apiView import *
from account.views import *

views = [
    path("signup", signup_view, name="signup"),
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    path("home", home_view, name="home"),
]

api_views = [
    path("api/signup", signup_api, name="signup_api"),
    path("api/login", login_api, name="login_api")
]

urlpatterns = api_views + views
