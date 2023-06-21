from django.db import models

# Create your models here.
class Restaurant(models.Model):
    restaurant_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=350)
    items = models.JSONField()
    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)
    full_details = models.JSONField()

    class meta:
        db_table = 'restaurant'

