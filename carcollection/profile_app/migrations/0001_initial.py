# Generated by Django 4.2.1 on 2023-05-21 12:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[django.core.validators.MinValueValidator(2, message='The username must be a minimum of 2 chars')])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(18)])),
                ('password', models.CharField(max_length=30)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('profile_picture', models.URLField(blank=True)),
            ],
        ),
    ]
