from django.urls import path
from .views import hello,contact,signup,loginview,home,signupview,proall,productview

urlpatterns = [
    path('',hello),
    path('contact/',contact,name='contact'),
    path('signup/',signup,name='signup'),
    path('login/',loginview,name='loginview'),
    path('home/',home,name='home'),
    path('register/',signupview,name='register'),
    path('view/<int:abc>/',productview,name='proview'),
    path('proall/',proall,name='proall')
]