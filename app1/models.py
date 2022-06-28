from datetime import date
from django.db import models

# Create your models here.

class subadmin(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=150)
    contact=models.IntegerField(default=0)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Signup(models.Model):
    n='slect gender'
    g = [
        (n, 'select gender'),

        ('Male', 'Male'),
        ('FEmale', 'female'),

    ]

    username=models.CharField(verbose_name='Enter your name',max_length=10)
    email=models.EmailField()
    ph_no=models.PositiveIntegerField()
    password=models.CharField(max_length=8)
    address=models.TextField(default="")
    status=models.BooleanField(default=False,verbose_name='Subscription done?')
    date=models.DateField(auto_now=True)
    gender=models.CharField(max_length=12,choices=g,default=n)
    def __str__(self):
        return self.username



class category(models.Model):
    name=models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline

class Register(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    contact=models.PositiveIntegerField()
    password=models.CharField(max_length=10)
