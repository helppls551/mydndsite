from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.info,name='info'),
    path('hero/<int:pk>', views.post_info, name='post_info'),
    path('hero_new',views.post_new,name='newhero')
]