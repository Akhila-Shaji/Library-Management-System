# Generated by Django 5.0.6 on 2024-06-12 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_rename_book_name_accepted_button_model_bookname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accepted_button_model',
            old_name='user',
            new_name='userDetails',
        ),
    ]
