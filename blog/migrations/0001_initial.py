# Generated by Django 4.2.13 on 2024-06-14 10:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
   
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name="post",
            fields=[
                ("id", models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),
                ("title", models.CharField(max_length=200)),
                ("des", models.CharField(max_length=200)),
                ("body", models.TextField()),
                ("date", models.DateTimeField( default=datetime.datetime(2024, 6, 14, 16, 26, 16, 99071))),
            ],
        ),
    ]
