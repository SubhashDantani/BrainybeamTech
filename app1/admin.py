from pyexpat import model
from django.contrib import admin
from .models import category, subadmin,Signup,Blog,Author,Entry,Register,Pro

# Register your models here.
admin.site.register(subadmin)
admin.site.register(category)
admin.site.register(Signup)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)

class Proadmin(admin.ModelAdmin):
    list_display=['name','price','des','review']
    list_filter=['name','price','des','review']
admin.site.register(Pro,Proadmin)
class REG(admin.ModelAdmin):
    list_display=['name','email','contact']
admin.site.register(Register,REG)

