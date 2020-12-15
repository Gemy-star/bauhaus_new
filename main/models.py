from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='الأسم')
    email = models.EmailField(null=True, blank=True, verbose_name='البريد الألكترونى')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='العنوان')
    message = models.CharField(max_length=255, null=True, blank=True, verbose_name='الرساله')

    def __str__(self):
        return self.name
