from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('check-email', views.check_email, name='check-email'),
    path('home-engineer', views.home_engineer, name='home-engineer'),
    path('register-engineer', views.registerEngineer, name='register-engineer'),
    path('register-customer', views.register_customer, name='register-customer'),
    path('register-outdoor', views.register_outdoorEngineer, name='register-outdoor'),

]
