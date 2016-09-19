import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
#serviceurl = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/geojson?'

# Use data "Bowling Green State University"
# For real test "University of Tartu"

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    #print json.dumps(js, indent=4)

    print "place_id:", js["results"][0]["place_id"]