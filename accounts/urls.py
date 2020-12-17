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
    path('user-detail', views.user_detail, name='user-detail'),
    path('change-status/<int:pk>', views.change_status, name='change-status'),
    path('engineer/<int:pk>', views.engineer_detail, name='engineer-detail'),
    path('emp-info', views.emp_info, name='emp-info'),

]
