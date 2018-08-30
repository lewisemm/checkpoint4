from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def index(request):
    """Display the login template."""
    return render(request, 'views/angular_base.html', {'request': request})