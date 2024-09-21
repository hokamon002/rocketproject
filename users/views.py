from django.http import HttpResponse

from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import login, logout

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form}) 

def login_view(request):
    return HttpResponse(b"Hello, world. You're at the polls index.")

def logout_view(request):
    return HttpResponse(b"Hello, world. You're at the polls index.")
