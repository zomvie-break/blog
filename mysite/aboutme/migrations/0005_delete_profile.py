# Generated by Django 4.2.1 on 2023-08-03 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0004_alter_profile_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
