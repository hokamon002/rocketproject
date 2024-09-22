from django.http import HttpResponse

from django.shortcuts import render, redirect 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import TeamRegistrationForm


def register_view(request):
    if request.method == "POST":
        form = TeamRegistrationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("")
    else:
        form = TeamRegistrationForm()
    return render(request, "users/register.html", { "form": form })

def login_view(request):
    return HttpResponse(b"Hello, world. You're at the polls index.")

def logout_view(request):
    return HttpResponse(b"Hello, world. You're at the polls index.")
