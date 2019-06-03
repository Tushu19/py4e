'''
Calling a JSON API

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. 
The program will 
* prompt for a location, 
* contact a web service 
* and retrieve JSON for the web service 
* and parse that data, 
* and retrieve the first place_id from the JSON. 

A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

API End Points

To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

http://py4e-data.dr-chuck.net/json?

This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. 
If you visit the URL with no parameters, you get "No address..." response.
To call the API, you need to provide address that you are requesting as the address= parameter that is properly URL encoded using the urllib.urlencode() fuction as shown in http://www.py4e.com/code3/geojson.py

Test Data / Sample Execution

You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJNeHD4p-540AR2Q0_ZjwmKJ8".

$ python3 solution.py
Enter location: South Federal University
Retrieving http://...
Retrieved 2021 characters
Place id ChIJNeHD4p-540AR2Q0_ZjwmKJ8

Turn In

Please run your program to find the place_id for this location:

Instituto Tecnologico de Santo Domingo
Make sure to enter the name and case exactly as above and enter the place_id and your Python code below. 
Hint: The first seven characters of the place_id are "ChIJ44v ..."
Make sure to retreive the data from the URL specified above and not the normal Google API. 
Your program should work with the Google API - but the place_id may not match for this assignment.
'''

import urllib.request, urllib.parse, urllib.error
import json
import ssl
import sys

def main():
    (service_url, api_key) = get_service_details()
    target_location = prompt_location()
    query_url = construct_query_url(service_url, target_location, api_key)
    url_handle = open_url(query_url)
    url_data_string = get_data_from_url(url_handle)
    geo_api_json = read_string_to_json(url_data_string)
    print('Place id', extract_place_id(geo_api_json))
    return

def prompt_location():
    target_location = input('Enter location: ')
    return target_location

def get_service_details():
    api_key = False
    # If you have a Google Places API key, enter it here
    # api_key = 'AIzaSy___IDByT70'
    # https://developers.google.com/maps/documentation/geocoding/intro

    if api_key is False:
        api_key = 42
        service_url = 'http://py4e-data.dr-chuck.net/json?'
    else :
        service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

    return (service_url, api_key)

def construct_query_url(servie_url, target_location, api_key):
    parameter_dict = dict()
    parameter_dict['address'] = target_location
    parameter_dict['key'] = api_key

    query_url = servie_url + urllib.parse.urlencode(parameter_dict)

    return query_url

def open_url(url):
    ssl_context = set_ssl_context_to_ignore()

    print('Retrieving', url)

    url_handle = urllib.request.urlopen(url, context=ssl_context)

    return url_handle

def set_ssl_context_to_ignore():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx

def get_data_from_url(url_handle):
    url_data = url_handle.read()
    print('Retrieved', len(url_data), 'characters')
    return url_data

def read_string_to_json(data_string):
    try:
        js = json.loads(data_string)
    except:
        js = None

    # DEBUG
    #print(json.dumps(js, indent=4))
    # /DEBUG

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data_string)
        sys.exit(2)

    return js

def extract_place_id(geo_api_json):
    return geo_api_json['results'][0]['place_id']

if __name__ == "__main__":
    main()