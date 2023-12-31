# Generated by Django 5.0 on 2023-12-31 02:15

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ToDo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("date", models.DateField()),
                ("description", models.CharField(max_length=1000)),
                ("category", models.CharField(max_length=100)),
                ("completed", models.BooleanField()),
            ],
        ),
    ]
