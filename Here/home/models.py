from django.db import models

try:
    # Django versions >= 1.9
    from django.utils.module_loading import import_module
except ImportError:
    # Django versions < 1.9
    from django.utils.importlib import import_module


# Create your models here.

class register_case(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=50)
    vehical_no = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=50)
    dob = models.DateField()
    case_date = models.DateField()
    case_resgister = models.DateField()
    reasone = models.TextField()
    address = models.CharField(max_length=300)
    lat = models.FloatField()
    long = models.FloatField()

    Accident = "Accident"
    Murder = "Murder"
    Rape = "Rape"

    case_type_choice = (
        (Accident, "Accident"),
        (Murder, "Murder"),
        (Rape, "Rape"),
    )

    case_type = models.CharField(max_length=9, choices=case_type_choice, default="JANUARY")
