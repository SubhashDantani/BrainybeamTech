from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("welcome to website")

def contact(request):
    return HttpResponse("welcome to contact page")

def signup(request):
    return render(request,'pages/signup.html')

def login(request):
    a="hello"
    cal=6+7
    return render(request,'pages/login.html',{'q':a,'c':cal})

def home(request):
    return render(request,'pages/home.html')