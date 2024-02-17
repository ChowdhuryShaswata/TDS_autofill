from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import TDSUser, NameGenerator
from .prepopulate import load_initial_namegenerator_data
from .query import autofillUser, createUser

# Create your views here.
def index(request):
    
    return render(request, 'authentication/registration.html', {})

def register_user(request):
    try:
        load_initial_namegenerator_data()
    except:
        pass
        
    new_username = ''
    new_email = ''
    new_password = ''

    if request.method=="GET" and 'autofill_button' in request.GET:
        new_username, new_email, new_password = autofillUser()
    
    if request.method=="POST":
        name = request.POST['username']
        email = request.POST['email_address']
        password = request.POST['password']
        createUser(username=name, password=password, email=email)

    return render(request, 'registration/login.html', {'new_username': new_username, 'new_email': new_email, 'new_password': new_password})