# Generated by Django 4.2.1 on 2023-06-05 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.CharField(default='nothing', max_length=1000),
            preserve_default=False,
        ),
    ]
