from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Signup,Entry,Register,Pro
from django.db.models import Q

# Create your views here.
def hello(request):
    a=Signup.objects.all()
    b=Entry.objects.all()
    return render(request,'pages/index.html',{'s':a,'r':b})

def searchview(request):
    q=request.GET.get('search')
    if q:
        pr=Pro.objects.filter(Q(name__icontains=q)| Q(des__icontains=q) |Q(price__icontains=q))
        data={'p':pr}
    else:
        data={}
    return data

def contact(request):
    return HttpResponse("welcome to contact page")

def signup(request):
    return render(request,'pages/signup.html')

def home(request):
    s=searchview(request)
    return render(request,'pages/home.html',s)

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

def productdelete(request,abc):
    v=Pro.objects.get(id=abc)
    v.delete()
    return redirect('proall')

def proall(request):
    if 'xyz' in request.session.keys():
        l=Pro.objects.all()
        return render(request,'proall.html',{'l':l})
    else:
        return redirect('loginview')

def loginview(request):
    if request.method=='POST':
        try:
            print("123")
            m=Signup.objects.get(email=request.POST['email'])
            print(m)
            if m.password==request.POST['pass']:
                request.session['xyz']=m.id
                print("pass")

                return redirect('proall')
            else:
                return HttpResponse("wrong password")
        except:
            return HttpResponse("wrong email")
    return render(request,'pages/login.html')

def aboutview(request):
    return render(request,'pages/about.html')

def logout(request):
    if 'xyz' in request.session.keys():
        del request.session['xyz']
        return redirect('loginview')
    else:
        return redirect('loginview')
    
def productadd(request):
    if request.method=='POST':
        model=Pro(request.POST)
        model.name=request.POST['name']
        model.des=request.POST['des']
        model.img=request.FILES.get('image')
        model.save()
