# Generated by Django 4.2.2 on 2023-06-21 17:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("searchengine", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="restaurant",
            old_name="locaton",
            new_name="location",
        ),
    ]
