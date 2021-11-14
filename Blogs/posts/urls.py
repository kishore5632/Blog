from django.urls import path
from posts.views import *

urlpatterns = [
    #path('category',post_us,name='category'),
    path('contact',Contact,name='contact'),
    path('',index,name='index'),
    path('single/<slug:slug>',single_us,name='single'),
    path('login',login_view,name='login'),
    path('Signup',Signup_view,name='Signup'),
    path('logout',user_logout,name="logout"),
    path('search/', search, name='search'),
    
]
