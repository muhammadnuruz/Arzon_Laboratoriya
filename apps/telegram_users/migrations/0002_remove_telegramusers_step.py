# Generated by Django 5.0.1 on 2024-09-22 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telegramusers',
            name='step',
        ),
    ]