from django.contrib import admin
from .models import EngineerStatus, RequestWorkOfCustomer, RequestWorkOfEngineer, Work, Reply

admin.site.register(EngineerStatus)
admin.site.register(Work)
admin.site.register(RequestWorkOfEngineer)
admin.site.register(RequestWorkOfCustomer)
admin.site.register(Reply)
