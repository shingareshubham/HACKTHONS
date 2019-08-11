from django.db import models
import pandas as pd
from home.models import register_case

# Create your models here.
from django_pandas.io import read_frame
qs = register_case.objects.all()
#df = read_frame(qs)

