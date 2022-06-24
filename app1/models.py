from django.db import models

# Create your models here.

class subadmin(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=150)
    contact=models.IntegerField(default=0)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.name



class category(models.Model):
    name=models.CharField(max_length=100)


    def __str__(self):
        return self.name


