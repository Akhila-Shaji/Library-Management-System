# Generated by Django 5.0.6 on 2024-06-12 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_accepted_button_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accepted_button_model',
            old_name='book_name',
            new_name='bookname',
        ),
    ]
