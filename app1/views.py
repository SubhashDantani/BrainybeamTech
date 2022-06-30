from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Signup,Entry,Register,Pro

# Create your views here.
def hello(request):
    a=Signup.objects.all()
    b=Entry.objects.all()
    return render(request,'pages/index.html',{'s':a,'r':b})

def contact(request):
    return HttpResponse("welcome to contact page")

def signup(request):
    return render(request,'pages/signup.html')

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
        return redirect('login')
    return render(request,'pages/register.html')

def productview(request,abc):
    v=Pro.objects.get(id=abc)
    return render(request,'productview.html',{'v':v})

def proall(request):
    l=Pro.objects.all()
    return render(request,'proall.html',{'l':l})

def loginview(request):
    if request.method=='POST':
        try:
            print("123")
            m=Signup.objects.get(email=request.POST['email'])
            print(m)
            if m.password==request.POST['pass']:
                print("pass")
                return redirect('proall')
            else:
                return HttpResponse("wrong password")
        except:
            return HttpResponse("wrong email")
    return render(request,'pages/login.html')

