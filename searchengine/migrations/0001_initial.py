# Generated by Django 4.2.2 on 2023-06-21 17:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Restaurant",
            fields=[
                (
                    "restaurant_id",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=300)),
                ("locaton", models.CharField(max_length=350)),
                ("items", models.JSONField()),
                ("latitude", models.DecimalField(decimal_places=10, max_digits=15)),
                ("longitude", models.DecimalField(decimal_places=10, max_digits=15)),
                ("full_details", models.JSONField()),
            ],
        ),
    ]