from django.contrib import admin
from django.urls import path
from web.views import *

urlpatterns = [
    path('', main_view, name='main'),
    path('home', main_view, name='main'),
    path('registration/', registration_view, name='registration'),
    path('auth/', auth_view, name='auth'),
    path('logout/', logout_view, name='logout'),
    path('cars/', cars_view, name='cars'),
    path('car/add', add_car_view, name='add_car'),
    path('car/<int:id>', car_view, name='car'),
    path('blog/', blog_view, name='blog'),
    path('post/<int:id>', post_view, name='post'),
    path('post/add', create_post_view, name='create_post')
]
