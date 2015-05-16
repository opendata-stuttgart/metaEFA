import logging
import time
import requests

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
    url += 'zocationServerActive=%d' % zocationServerActive
    url += '&lsShowTrainsExplicit%d' % lsShowTrainsExplicit
    url += '&stateless=%d' % stateless
    url += '&language=%s' % language
    url += '&SpEncId=%d' % SpEncId
    url += '&anySigWhenPerfectNoOtherMatches=%d'\
        % anySigWhenPerfectNoOtherMatches
    url += '&limit=%d' % limit
    url += '&depArr=%s' % depArr
    url += '&type_dm=%s' % type_dm
    url += '&anyObjFilter_dm=%d' % anyObjFilter_dm
    url += '&deleteAssignedStops=%d' % deleteAssignedStops
    url += '&name_dm=%s' % name_dm
    url += '&mode=%s' % mode
    url += '&dmLineSelectionAll=%d' % dmLineSelectionAll
    url += '&itdDateYear=%d' % itdDateYear
    url += '&itdDateMonth=%d' % itdDateMonth
    url += '&itdDateDay=%d' % itdDateDay
    url += '&itdTimeHour=%d' % itdTimeHour
    url += '&itdTimeMinute=%d' % itdTimeMinute
    url += '&useRealtime=%d' % useRealtime
    url += '&outputFormat=%s' % outputFormat

    efa = requests.get(url).json()
    return efa
