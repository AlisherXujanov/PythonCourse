
import json

import requests  # to install: pip install requests


def find_person_by_ip(ip_address):
    url = "http://ip-api.com/json/"
    response = requests.get(url, ip_address)
    data = json.loads(response.content)
    return data


# type ipconfig in cmd
# ----------------------------------------------------------------
# /=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=
# ----------------------------------------------------------------
my_ip_address = "192.168.0.109"
# 192.168.0.109
# 'lat': 39.6588, 'lon': 66.9615,

# ----------------------------------------------------------------
# /=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=
# ----------------------------------------------------------------

# JS to get IP address:

# fetch('https://api.ipify.org?format=json')
#   .then(response => response.json())
#   .then(data => console.log(data.ip))
#   .catch(error => console.error('Error:', error));
# 213.230.87.154
# 'lat': 39.6588, 'lon': 66.9615
# ----------------------------------------------------------------
# /=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=
# ----------------------------------------------------------------
geolocation_data = find_person_by_ip(my_ip_address)
print(geolocation_data)
