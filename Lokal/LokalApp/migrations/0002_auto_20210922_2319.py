# Generated by Django 3.2.6 on 2021-09-22 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LokalApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='last_name',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='phone_number',
            new_name='phonenumber',
        ),
    ]