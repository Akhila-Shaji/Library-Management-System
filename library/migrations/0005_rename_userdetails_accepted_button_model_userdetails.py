# Generated by Django 5.0.6 on 2024-06-12 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_rename_user_accepted_button_model_userdetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accepted_button_model',
            old_name='userDetails',
            new_name='userdetails',
        ),
    ]