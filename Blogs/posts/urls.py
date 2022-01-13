from django.urls import path,include
from posts.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Poster',PosterViewset)



urlpatterns = [
    #path('category',post_us,name='category'),
    path('', include(router.urls)),
    path('contact',Contact,name='contact'),
    path('index',index,name='index'),
    path('single/<slug:slug>',single_us,name='single'),
    path('login',login_view,name='login'),
    path('Signup',Signup_view,name='Signup'),
    path('logout',user_logout,name="logout"),
    path('search/', search, name='search'),
    #api url
    path('poster',poster_view.as_view()),
    path('category',Categoryview.as_view()),
    path('category_add',Category_create.as_view()),
    path('category/<int:pk>',Category_update_delete.as_view()),
    path('contacts',contactview.as_view()),
    path('contacts/<int:pk>',contactview_read_delete.as_view()),
    path('comment',Commentview.as_view()),
    path('comment/<int:pk>',Comment_view_delete.as_view()),
    path('author',Authorview.as_view()),
    path('author/<int:pk>', Author_update_delete.as_view()),
    
]
