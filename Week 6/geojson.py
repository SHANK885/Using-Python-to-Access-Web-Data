import urllib.parse
import urllib.request
import json

place_name = 'University of Tuebingen'
base_url = "http://py4e-data.dr-chuck.net/json?sensor=false&"
address_param = urllib.parse.urlencode({'address': place_name})
target = base_url + address_param

print("Retrieving {0}".format(target))
connection = urllib.request.urlopen(target)
raw_data = connection.read()
print("Retrieved {0} characters".format(len(raw_data)))
parsed_data = json.loads(raw_data)
print(parsed_data)

print("Place id", parsed_data["results"][0]["place_id"])