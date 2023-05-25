from django.contrib import admin
from . import models

my_models= [models.Item, models.Brand]
admin.site.register(my_models)
