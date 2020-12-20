# Generated by Django 3.1.4 on 2020-12-20 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('office', '0008_bestengineer_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestworkofcustomer',
            name='service',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'طلب عمل'), (2, 'طلب مقايسه')], null=True, verbose_name='نوع الطلب'),
        ),
        migrations.AddField(
            model_name='requestworkofengineer',
            name='service',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'طلب عمل'), (2, 'طلب مقايسه')], null=True, verbose_name='نوع الطلب'),
        ),
        migrations.AddField(
            model_name='work',
            name='service',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'طلب عمل'), (2, 'طلب مقايسه')], null=True, verbose_name='نوع الطلب'),
        ),
        migrations.CreateModel(
            name='EngineerInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv', models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='السى فى ')),
                ('min_pay', models.IntegerField(blank=True, null=True, verbose_name='اق سعر')),
                ('max_pay', models.IntegerField(blank=True, null=True, verbose_name='أكثر سعر')),
                ('certificate', models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='شهادة التخرج')),
                ('engineer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='المهندس')),
            ],
            options={
                'verbose_name': ' بيانات اضافيه - مهندس',
                'verbose_name_plural': 'افضل مهندسين - الشهر',
                'ordering': ['engineer'],
            },
        ),
    ]
