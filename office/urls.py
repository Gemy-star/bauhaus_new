from django.urls import path
from . import views

urlpatterns = [
    path('engineer-list', views.engineer_online_list, name='engineer-online-list'),
    path('request/work/<int:pk>', views.request_work_engineer, name='cus-request-eng'),
    path('request-list', views.request_list_engineer, name='request-engineer-work-list'),
    path('request-list/customer', views.request_work_customer, name='request-customer-work-list'),
    path('send-message-customer/<str:email>', views.send_to_customer, name='send-to-customer'),
    path('send-message-engineer/<str:email>', views.send_to_engineer, name='send-to-engineer'),
    path('customer/inbox', views.customer_messages_list, name='customer-inbox'),
    path('engineer/inbox', views.engineer_messgae_list, name='engineer-inbox'),
    path('engineer/best', views.best_engineer, name='engineer-best'),
    path('engineer/info', views.add_info, name='add-info'),
    path('request/cycle', views.cycle_request, name='cycle-request'),
    path('services/all', views.services, name='services-all'),
    path('etlob', views.etlob_service, name='etlob'),
    path('dash-service', views.services_dash, name='dash-service'),
    path('etlob/services/<int:pk>', views.Etlob_service, name='etlob-per-service'),

]
