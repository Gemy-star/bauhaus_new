from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('contact', views.contact_ajax, name='contact-ajax')
]
