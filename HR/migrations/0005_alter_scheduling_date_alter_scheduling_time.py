# Generated by Django 5.1.6 on 2025-02-28 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0004_alter_scheduling_date_alter_scheduling_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduling',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='scheduling',
            name='time',
            field=models.TimeField(),
        ),
    ]
