from django.urls import path
from .views import hello,contact,signup,login,home

urlpatterns = [
    path('',hello),
    path('contact/',contact,name='contact'),
    path('signup/',signup,name='signup'),
    path('login/',login,name='login'),
    path('home/',home,name='home')
]