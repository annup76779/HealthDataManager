import json

from rest_framework.response import Response

from .models import User
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view

from .serializers import UserSerializer


@api_view(["POST"])
def signup_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        role = data.get('role')
        username = data.get('username')
        password = data.get('password')

        # Basic validation and user creation logic
        if User.objects.filter(username=username).exists():
            return Response({'username': ['Username is already taken.']}, status=400)

        user = User.objects.create_user(username=username, password=password, role=role, first_name=name)
        user.save()
        return Response({'detail': 'Signup successful'}, status=200)

    return Response({'detail': 'Invalid request'}, status=405)


@api_view(["POST"])
def login_api(request):
    if request.method == 'POST':
        data = request.data

        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            return Response({"detail": "Invalid username or password"}, status=401)

        login(request, user)
        user_srlz = UserSerializer(instance=user)
        return Response({'detail': 'Login successful', **user_srlz.data}, status=200)

    return Response({'detail': 'Invalid request'}, status=405)
