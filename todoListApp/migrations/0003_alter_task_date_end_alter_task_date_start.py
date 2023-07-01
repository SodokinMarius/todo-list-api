# Generated by Django 4.1.5 on 2023-07-01 19:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoListApp', '0002_task_file_alter_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_start',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]