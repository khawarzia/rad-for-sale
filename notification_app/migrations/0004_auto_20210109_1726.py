# Generated by Django 2.2 on 2021-01-09 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification_app', '0003_auto_20210109_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification_model',
            name='date_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]