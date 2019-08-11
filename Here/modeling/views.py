from django.shortcuts import render
from .models import titanic, loaded_model, df

# Create your views here.
def models(request):
    models_ = titanic.objects.all()
    return render(request,"models.html", {'models_':models_})