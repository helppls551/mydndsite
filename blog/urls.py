from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.info,name='info'),
    path('hero/<int:pk>', views.post_info, name='post_info'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('post/<pk>/del/', views.post_del, name='post_del'),
    path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('hero_new',views.post_new,name='newhero')
]