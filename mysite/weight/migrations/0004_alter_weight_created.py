# Generated by Django 4.2.1 on 2023-09-13 05:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weight', '0003_alter_weight_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 13, 5, 27, 26, 761911, tzinfo=datetime.timezone.utc)),
        ),
    ]