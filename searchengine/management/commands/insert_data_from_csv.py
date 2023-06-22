from typing import Any, Optional
import pandas as pd
import json
from django.core.management import BaseCommand
from searchengine.models import Restaurant


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from children.csv"

    def handle(self, *args: Any, **options: Any) -> str | None:
        if Restaurant.objects.exists():
            print("data is already  present in the database")
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        print("loading the data", end="")

        data_df = pd.read_csv("restaurants_small.csv")

        for _, i in data_df.iterrows():
            restaurant_id, name, location, items, lat_long, full_details = i
            items = json.loads(items)
            full_details = json.loads(full_details)
            latitude, longitude = list(map(float, lat_long.split(",")))
            x = Restaurant(
                restaurant_id=restaurant_id,
                name=name,
                location=location,
                items=items,
                latitude=latitude,
                longitude=longitude,
                full_details=full_details,
            )
            x.save()
            print(".", end="")
        print("done")
