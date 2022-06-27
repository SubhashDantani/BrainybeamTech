from pyexpat import model
from django.contrib import admin
from .models import category, subadmin,Signup,Blog,Author,Entry

# Register your models here.
admin.site.register(subadmin)
admin.site.register(category)
admin.site.register(Signup)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)

