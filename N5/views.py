from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render

from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import RegisterSerializer

class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer