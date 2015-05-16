import logging
import requests
from datetime import datetime

from main.models import Station
import csv


def populate_stations(path='/opt/code/vvs_data/HaltestellenVVS_simplified_utf8_stationID.csv'):
    """
    parse simplified csv, add elements to database
    """
    with open(path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        # skip first row
        next(reader, None)
        for row in reader:
            obj, created = Station.objects.update_or_create(
                station_id=row[0], defaults={
                    'name': row[1],
                    'full_name': row[2]
                }
            )

            if created:
                logging.info("Created station %s" % row[0])
            else:
                logging.info("Updated station %s" % row[0])


def get_EFA_from_VVS(station_id):
    """
    send HTTP Request to VVS and return a xml string
    """
    # parameters needed for EFA
    zocationServerActive = 1
    lsShowTrainsExplicit = 1
    stateless = 1
    language = 'de'
    SpEncId = 0
    anySigWhenPerfectNoOtherMatches = 1
    # max amount of arrivals to be returned
    limit = 30
    depArr = 'departure'
    type_dm = 'any'
    anyObjFilter_dm = 2
    deleteAssignedStops = 1
    name_dm = station_id
    mode = 'direct'
    dmLineSelectionAll = 1
    useRealtime = 1
    outputFormat = 'json'
    coordOutputFormat = 'WGS84[DD.ddddd]'

    url = 'http://www2.vvs.de/vvs/widget/XML_DM_REQUEST?'
    url += 'zocationServerActive={:d}'.format(zocationServerActive)
    url += '&lsShowTrainsExplicit{:d}'.format(lsShowTrainsExplicit)
    url += '&stateless={:d}'.format(stateless)
    url += '&language={}'.format(language)
    url += '&SpEncId={:d}'.format(SpEncId)
    url += '&anySigWhenPerfectNoOtherMatches={:d}'.format(
        anySigWhenPerfectNoOtherMatches
    )
    url += '&limit={:d}'.format(limit)
    url += '&depArr={}'.format(depArr)
    url += '&type_dm={}'.format(type_dm)
    url += '&anyObjFilter_dm={:d}'.format(anyObjFilter_dm)
    url += '&deleteAssignedStops={:d}'.format(deleteAssignedStops)
    url += '&name_dm={}'.format(name_dm)
    url += '&mode={}'.format(mode)
    url += '&dmLineSelectionAll={:d}'.format(dmLineSelectionAll)

    url += ('&itdDateYear={0:%Y}&itdDateMonth={0:%m}&itdDateDay={0:%d}' +
            '&itdTimeHour={0:%H}&itdTimeMinute={0:%M}').format(
                datetime.now())

    url += '&useRealtime={:d}'.format(useRealtime)
    url += '&outputFormat={}'.format(outputFormat)
    url += '&coordOutputFormat={}'.format(coordOutputFormat)

    r = requests.get(url)
    r.encoding = 'UTF-8'
    efa = r.json()
    return efa


def parse_efa(efa):
    parsedDepartures = []

    if not efa or "departureList" not in efa or not efa["departureList"]:
        return parsedDepartures

    for departure in efa["departureList"]:
        stopName = departure["stopName"]
        latlon = departure['y'] + "," + departure['x']
        number = departure["servingLine"]["number"]
        direction = departure["servingLine"]["direction"]

        if "realDateTime" in departure:
            realDateTime = departure["realDateTime"]
        elif "dateTime" in departure:
            realDateTime = departure["dateTime"]
        else:
            realDateTime = None

        if "servingLine" in departure and "delay" in departure["servingLine"]:
            delay = departure["servingLine"]["delay"]
        else:
            delay = 0

        departureObject = {
            "stopName": stopName,
            "number": number,
            "direction": direction,
            "departureTime": realDateTime,
            "delay": delay,
            "stationCoordinates": latlon
        }

        parsedDepartures.append(departureObject)

    return parsedDepartures
