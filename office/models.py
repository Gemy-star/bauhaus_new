from django.db import models
from accounts.models import User


class EngineerStatus(models.Model):
    STATUS_CHOCIES = (
        (1, 'متاح'),
        (2, 'غير متاح')
    )
    engineer = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, verbose_name='مهندس')
    status = models.SmallIntegerField(null=True, blank=True, choices=STATUS_CHOCIES)

    def __str__(self):
        return self.engineer.first_name


class RequestWorkOfEngineer(models.Model):
    customer_email = models.EmailField(max_length=255, blank=True, null=True, verbose_name='الأسم')
    request = models.TextField(verbose_name='الطلب', blank=True, null=True)
    engineer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='مهندس')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الأضافه')

    class Meta:
        ordering = ['customer_email', ]
        verbose_name = 'طلب العمل  مع مهندس'
        verbose_name_plural = 'طلبات العمل  مع مهندس '

    def __str__(self):
        return self.customer_email


class RequestWorkOfCustomer(models.Model):
    engineer_email = models.EmailField(max_length=255, blank=True, null=True, verbose_name='م/البريد الألكترونى')
    request = models.TextField(verbose_name='الطلب', blank=True, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='عميل')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الأضافه')

    def __str__(self):
        return self.customer.first_name

    class Meta:
        ordering = ['engineer_email', ]
        verbose_name = 'طلب العمل  من عميل'
        verbose_name_plural = 'طلبات العمل  إلى عميل  '


class Work(models.Model):
    request = models.TextField(verbose_name='الطلب', blank=True, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='عميل')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الأضافه')

    class Meta:
        ordering = ['customer', ]
        verbose_name = 'طلب عمل'
        verbose_name_plural = 'طلبات عمل'

    def __str__(self):
        return self.customer.first_name


class Reply(models.Model):
    reply_message = models.TextField(verbose_name='الرد', blank=True, null=True)
    sender = models.ForeignKey(User, related_name='%(class)s_requests_created', on_delete=models.CASCADE,
                               verbose_name='المرسل')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='المرسل إليه')

    class Meta:
        ordering = ['sender', ]
        verbose_name = ' رد على عميل'
        verbose_name_plural = 'ردود على عميل'

    def __str__(self):
        return self.engineer.first_name