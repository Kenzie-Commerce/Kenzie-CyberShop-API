# Generated by Django 4.2.1 on 2023-05-08 18:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("addresses", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="default",
            field=models.BooleanField(default=False),
        ),
    ]
