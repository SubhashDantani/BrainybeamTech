from django.urls import path
from .views import hello,contact, searchview,signup,logout,loginview,home,signupview,proall,productview,aboutview,productdelete
urlpatterns = [
    path('',hello),
    path('contact/',contact,name='contact'),
    path('signup/',signup,name='signup'),
    path('login/',loginview,name='loginview'),
    path('home/',home,name='home'),
    path('register/',signupview,name='register'),
    path('view/<int:abc>/',productview,name='proview'),
    path('del/<int:abc>/',productdelete,name='prodel'),

    path('proall/',proall,name='proall'),
    path('search/',searchview,name='search'),
    path('about/',aboutview,name='about'),
    path('logout/',logout,name='logout')
]