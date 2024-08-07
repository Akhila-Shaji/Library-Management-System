# Generated by Django 5.0.6 on 2024-06-12 04:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accepted_button_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50)),
                ('book_image', models.ImageField(upload_to='images/')),
                ('Author', models.CharField(max_length=50)),
                ('request_date', models.DateTimeField()),
                ('accepted_date', models.DateTimeField(auto_now_add=True)),
                ('fine', models.IntegerField(default=0)),
                ('return_date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.userdetails')),
            ],
        ),
    ]
