# Generated by Django 2.2 on 2021-01-09 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification_app', '0006_notification_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification_model',
            old_name='date_time',
            new_name='date',
        ),
    ]