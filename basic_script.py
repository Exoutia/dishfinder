import pandas as pd
import json
from django.core.management import BaseCommand
from searchengine.models import restaurant

data_df = pd.read_csv('restaurants_small.csv')

for _, i in data_df.iterrows():
    restaurant_id, name, location, items, lat_long, full_details = i
    items = json.loads(items)
    full_details = json.loads(full_details)
    latitude, longitude = list(map(float, lat_long.split(',')))
    restaurant(restaurant_id=restaurant_id, name=name, location=location, items=items, latitude=latitude, longitude=longitude, full_details=full_details)
    restaurant.save()
