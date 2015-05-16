import logging
import time
import requests

from main.models import Station
import csv, json


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
                station_id=row[0],
                name=row[1],
                full_name=row[2])

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
    limit = 5
    depArr = 'departure'
    type_dm = 'any'
    anyObjFilter_dm = 2
    deleteAssignedStops = 1
    name_dm = station_id
    mode = 'direct'
    dmLineSelectionAll = 1
    itdDateYear = int(time.strftime('%y'))
    itdDateMonth = int(time.strftime('%m'))
    itdDateDay = int(time.strftime('%d'))
    itdTimeHour = int(time.strftime('%H'))
    itdTimeMinute = int(time.strftime('%M'))
    useRealtime = 1
    outputFormat = 'json'

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
    url += '&itdDateYear={:d}'.format(itdDateYear)
    url += '&itdDateMonth={:d}'.format(itdDateMonth)
    url += '&itdDateDay={:d}'.format(itdDateDay)
    url += '&itdTimeHour={:d}'.format(itdTimeHour)
    url += '&itdTimeMinute={:d}'.format(itdTimeMinute)
    url += '&useRealtime={:d}'.format(useRealtime)
    url += '&outputFormat={}'.format(outputFormat)

    efa = requests.get(url).json()
    return efa

def parse_efa(efa):
    parsedDepartures = []
    
    for departure in efa["departureList"]:
        stopName = departure["stopName"]
        number = departure["servingLine"]["number"]
        direction = departure["servingLine"]["direction"]
        realDateTime = departure["realDateTime"]

        departureObject = {
            "stopName" : stopName,
            "number": number,
            "direction": direction,
            "departureTime": realDateTime          
        }

        parsedDepartures.append(departureObject)

    return parsedDepartures
