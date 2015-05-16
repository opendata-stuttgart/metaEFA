from meta_efa.models import Stations
import csv
datapath = ".././vvs_data/HaltestellenVVS_simplified_utf8_stationID.csv"
LOG = True

def populate_stations():
    with open(datapath, 'r') as f:
        reader = csv.reader(f, delimeter=',')
        #skip first row
        next(reader, None)
        for row in reader:
            obj, created = Stations.objects.update_or_create(
                station_id=row[0],
                name=row[1],
                full_name=row[2])

            if created:
                log("Created station %s" % row[0])
            else:
                log("Updated station %s" % row[0])


def log(message):
    if LOG:
        print(message)
