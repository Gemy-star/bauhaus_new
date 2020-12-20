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
    SERVICES_CHOICES = (
        (1, 'طلب عمل'),
        (2, 'طلب مقايسه')

    )
    service = models.SmallIntegerField(blank=True, null=True, choices=SERVICES_CHOICES, verbose_name='نوع الطلب')
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
    SERVICES_CHOICES = (
        (1, 'طلب عمل'),
        (2, 'طلب مقايسه')

    )
    service = models.SmallIntegerField(blank=True, null=True, choices=SERVICES_CHOICES, verbose_name='نوع الطلب')
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
    SERVICES_CHOICES = (
        (1, 'طلب عمل'),
        (2, 'طلب مقايسه')

    )
    service = models.SmallIntegerField(blank=True, null=True, choices=SERVICES_CHOICES, verbose_name='نوع الطلب')
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
        return self.sender.first_name


class BestEngineer(models.Model):
    engineer = models.ManyToManyField(User, null=True, verbose_name='المهندس')
    MONTH_CHOICES = (
        (1, 'يناير'),
        (2, 'فبراير'),
        (3, 'مارس'),
        (4, 'إبريل'),
        (5, 'مايو'),
        (6, 'يونيو'),
        (7, 'يوليو'),
        (8, 'أغسطس'),
        (9, 'سبمتمبر'),
        (10, 'أكتوبر'),
        (11, 'نوفمبر'),
        (12, 'ديسمبر'),
    )
    month = models.SmallIntegerField(blank=True, null=True, choices=MONTH_CHOICES, verbose_name='الشهر')
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['month', ]
        verbose_name = ' افضل مهندسين - الشهر'
        verbose_name_plural = 'افضل مهندسين - الشهر'

    def __str__(self):
        return str(self.month)


class EngineerInformation(models.Model):
    cv = models.FileField(upload_to='uploads/', null=True, blank=True, verbose_name="السى فى ")
    min_pay = models.IntegerField(null=True, blank=True, verbose_name='اق سعر')
    max_pay = models.IntegerField(null=True, blank=True, verbose_name='أكثر سعر')
    certificate = models.FileField(upload_to='uploads/', null=True, blank=True, verbose_name='شهادة التخرج')
    engineer = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='المهندس')
    detail = models.TextField(null=True, blank=True, verbose_name='نبذه')

    class Meta:
        ordering = ['engineer', ]
        verbose_name = ' بيانات اضافيه - مهندس'
        verbose_name_plural = 'افضل مهندسين - الشهر'

    def __str__(self):
        return self.engineer.first_name
