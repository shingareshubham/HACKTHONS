from django.urls import path

from . import views

urlpatterns = [
    path('accidental/', views.maps, name="maps"),
    path('criminal/', views.criminal, name="criminal"),
]