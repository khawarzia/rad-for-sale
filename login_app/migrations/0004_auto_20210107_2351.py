# Generated by Django 2.2 on 2021-01-07 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_auto_20210107_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='expiration',
        ),
        migrations.AddField(
            model_name='profile',
            name='expiration_month',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='expiration_year',
            field=models.IntegerField(default=2021),
        ),
    ]