# Generated by Django 3.1.4 on 2020-12-20 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0009_auto_20201220_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='engineerinformation',
            name='detail',
            field=models.TextField(blank=True, null=True, verbose_name='نبذه'),
        ),
    ]
