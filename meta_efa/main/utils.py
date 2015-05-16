import logging

from main.models import Station
import csv


def populate_stations(path='/opt/code/vvs_data/HaltestellenVVS_simplified_utf8_stationID.csv'):
    with open(path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        # skip first row
        next(reader, None)
        for row in reader:
            obj, created = Station.objects.update_or_create(
                station_id=row[0],
                name=row[1],
                full_name=row[2])

            if created:
                logging.info("Created station %s" % row[0])
            else:
                logging.info("Updated station %s" % row[0])
