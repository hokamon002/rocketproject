from django.contrib import admin

# Register your models here.
from .models import Team, Student

admin.site.register(Team)
admin.site.register(Student)
