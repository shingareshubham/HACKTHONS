from django.shortcuts import render


# Create your views here.

def maps(request):
    pr = "hello World"
    return render(request,"maps.html", {'pr':pr})

def criminal(request):
    return render(request,"criminal.html")