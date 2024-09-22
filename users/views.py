from django.http import HttpResponse

from django.shortcuts import render, redirect 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import TeamRegistrationForm
from .models import Student, Team


def register_view(request):
    if request.method == "POST":
        form = TeamRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            team = None
            if request.POST.get('team-register') == 'new':
                team_name = request.POST.get('enter-team-name')
                team = Team(name=team_name)
                team.save()
            else:
                team = form.cleaned_data.get('team')

            Student.objects.create(user=user, team = team)
            login(request, form.save())
            # return redirect("")
    else:
        form = TeamRegistrationForm()
    return render(request, "users/register.html", { "form": form })

def login_view(request):
    return HttpResponse(b"Hello, world. You're at the polls index.")

def logout_view(request):
    return HttpResponse(b"Hello, world. You're at the polls index.")
