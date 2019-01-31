import json
import urllib.parse, urllib.request

while True:
    loc = input('Enter location: ')
    if len(loc)<1: break

    baseurl = "http://py4e-data.dr-chuck.net/geojson?"
    url = baseurl + urllib.parse.urlencode({'sensor':'false', 'address':loc})
    print("Retrieving", url)

    data = urllib.request.urlopen(url).read()
    print("Retrieved ",len(data)," characters")

    jsonData = json.loads(data)

    # print json.dumps(jsonData, indent=4)
    print(jsonData["results"][0]["place_id"])