# Generated by Django 5.0 on 2023-12-31 02:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]