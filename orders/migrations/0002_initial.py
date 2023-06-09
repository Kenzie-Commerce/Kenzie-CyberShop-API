# Generated by Django 4.2.1 on 2023-05-08 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("orders", "0001_initial"),
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders",
                to="products.product",
            ),
        ),
    ]
