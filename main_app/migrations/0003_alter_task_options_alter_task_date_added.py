# Generated by Django 4.1.4 on 2023-01-11 21:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0002_alter_task_completed_alter_task_date_added"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["due_date", "-priority"]},
        ),
        migrations.AlterField(
            model_name="task",
            name="date_added",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 1, 11, 16, 29, 11, 463630)
            ),
        ),
    ]
