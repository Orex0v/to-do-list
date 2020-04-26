from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post_complte_add/<int:pk>/', views.post_complite, name='add'),
    path('complite_post_list', views.complite_post_list, name='complite'),
    path('signup', views.signup, name="signup")
    


]