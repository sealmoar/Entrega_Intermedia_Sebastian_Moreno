# Generated by Django 4.1.2 on 2022-10-29 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='location_name',
            new_name='name',
        ),
    ]
