# Generated by Django 2.2 on 2021-01-09 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification_model',
            name='not_type',
            field=models.BooleanField(default=True),
        ),
    ]