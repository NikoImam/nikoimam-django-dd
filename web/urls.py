from django.contrib import admin
from django.urls import path
from web.views import *

urlpatterns = [
    path('', main_view, name='main'),
    path('home', main_view, name='main'),
    path('registration/', registration_view, name='registration'),
    path('auth/', auth_view, name='auth'),
    path('logout/', logout_view, name='logout'),
    path('blog/', blog_view, name='blog'),
    path('post/', post_view, name='post'),
    path('createPost/', create_post_view, name='create_post')
]
