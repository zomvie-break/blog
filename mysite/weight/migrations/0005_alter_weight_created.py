# Generated by Django 4.2.1 on 2023-09-13 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weight', '0004_alter_weight_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='created',
            field=models.DateTimeField(),
        ),
    ]
