# Generated by Django 5.0.2 on 2024-04-13 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication_App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
    ]
