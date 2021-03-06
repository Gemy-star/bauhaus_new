# Generated by Django 3.1.4 on 2020-12-18 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('office', '0004_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='BestEngineer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField(choices=[(1, 'يناير'), (2, 'فبراير'), (3, 'مارس'), (4, 'إبريل'), (5, 'مايو'), (6, 'يونيو'), (7, 'يوليو'), (8, 'أغسطس'), (9, 'سبمتمبر'), (10, 'أكتوبر'), (11, 'نوفمبر'), (12, 'ديسمبر')])),
                ('engineer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
