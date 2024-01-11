from django.shortcuts import render
from .models import Projects

# Create your views here.
def user(request):
    projects = Projects.objects
    return render(request,'projects/user.html', {'Projects':projects})
