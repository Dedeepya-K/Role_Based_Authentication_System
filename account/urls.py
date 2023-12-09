from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('register', views.register, name='register'),
    path('home', views.home, name='home'),
    path('adminpage/', views.admin, name='adminpage'),
    path('patient/', views.patient, name='patient'),
    path('doctor/', views.doctor, name='doctor'),
    path('logout/', views.logout_view, name='logout_view'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
