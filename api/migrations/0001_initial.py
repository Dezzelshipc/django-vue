# Generated by Django 4.0.4 on 2022-06-29 11:26

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=128)),
                ('telegram', models.JSONField(default=list)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('data', models.JSONField(default=api.models.default_data)),
            ],
        ),
    ]
