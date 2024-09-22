from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.apps import apps

class TeamRegistrationForm(UserCreationForm):
    team_model = apps.get_model('users', 'Team')
    team = forms.ModelChoiceField(queryset=team_model.objects.all(), empty_label="Select a team")
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'team')  # Add team here


