from django.contrib.auth import authenticate
from django.http import HttpResponse

from .models import Account
from django.views.decorators.csrf import csrf_exempt          # this is for excemting the csrf token
import json


def index(request, *argv):
    return  HttpResponse("Hello World")

@csrf_exempt
def register(request):
    data = json.loads(request.body)
    if request.method == "POST":
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')
        user = Account.objects.create_superuser(email, username, password)
        print("=======================", user)
        return HttpResponse(user)
    # if the form is invalid
    else:
        return HttpResponse("Error")

@csrf_exempt
def login(request):
    data = json.loads(request.body)
    if request.method == "POST":
        email = data.get('email')
        password = data.get('password')
        user = authenticate(username=email, password=password)  # Authenticate
        print("=======================", user)
        if user:
            return HttpResponse("Login Success..")
        else:
            return HttpResponse("Login Fail..")
    else:
        return HttpResponse("Error")