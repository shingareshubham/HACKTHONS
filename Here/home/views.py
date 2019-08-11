from django.shortcuts import render
from .models import register_case

# Create your views here.

def index(request):
    case = register_case.objects.all()
    return render(request,"index.html",{'case': case})


def accident(request):
    return render(request,"accident.html")
