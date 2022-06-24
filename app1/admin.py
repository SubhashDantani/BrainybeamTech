from pyexpat import model
from django.contrib import admin

from .models import category, subadmin

# Register your models here.
admin.site.register(subadmin)
admin.site.register(category)



