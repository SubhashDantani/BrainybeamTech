from django.shortcuts import render
from django.http import HttpResponse
from .models import Signup,Entry,Register

# Create your views here.
def hello(request):
    a=Signup.objects.all()
    b=Entry.objects.all()
    return render(request,'pages/index.html',{'s':a,'r':b})

def contact(request):
    return HttpResponse("welcome to contact page")

def signup(request):
    return render(request,'pages/signup.html')

def login(request):
    return render(request,'pages/login.html',)

def home(request):
    return render(request,'pages/home.html')

def signupview(request):
    if request.method=='POST':
        model=Register()
        model.name=request.POST['name']
        model.email=request.POST['username']
        model.contact=request.POST['contact']
        model.password=request.POST['password']
        model.save()
    return render(request,'pages/register.html')