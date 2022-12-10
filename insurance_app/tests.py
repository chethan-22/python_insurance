from django.test import TestCase
from .admin import *

# Create your tests here.

def user_logout(request):
    logout(request)
    return redirect('index')
