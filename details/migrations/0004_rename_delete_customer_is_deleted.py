# Generated by Django 5.1.5 on 2025-01-29 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0003_rename_city_name_city_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='delete',
            new_name='is_deleted',
        ),
    ]
