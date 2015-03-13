# Project 3: MapQuest API Example Parse JSON

import urllib.request
import urllib.error
import urllib.parse 
import json

APP_KEY = 'Fmjtd%7Cluu82luanl%2C72%3Do5-948x04'
URL = 'http://open.mapquestapi.com/directions/v2/route?key={}&'.format(APP_KEY)

def format_url(start_loc:str, end_loc:str)->str:
    '''Takes in a start and end location and returns a url string formatted
    with the inputs'''
    query_parameters = [('from', start_loc), ('to', end_loc)]
    url_encode = urllib.parse.urlencode(query_parameters)
    return (URL + url_encode)
    
def get_result(url:str)->'json':
    '''Takes in a url and returns a Python object representing the parsed JSON
    result'''
    response = None
    try:
        response = urllib.request.urlopen(url)
        # Converts response to JSON format 
        json_text = response.read().decode(encoding = 'utf-8')
        # Converts into Python object 
        return json.loads(json_text)
    except urllib.error.HTTPError as e:
        print('Failed to download contents of URL')
        print('Status code: {}'.format(e.code))
        print()
    finally:
        if response != None:
            response.close()

def print_steps(json_result:'json')->None:
    '''Takes a parsed JSON response and prints the directions / steps'''
    step_list = json_result['route']['legs']
    for i in step_list:
        for j in i['maneuvers']:
            print(j['narrative'])

def print_distance(json_result:'json')->None:
    '''Takes a parsed JSON response and prints the total distance'''
    print(json_result['route']['distance'])

def print_time(json_result:'json')->None:
    '''Takes a parsed JSON response and prints the total time'''
    seconds = json_result['route']['time']
    print(seconds/60)

def map_direction(parameter:str, n:float)->str:
    '''Takes in a latitude or longitude value and determines the direction'''
    if parameter == 'lat':
        if n <= 90:
            return '{}N'.format(n)
        return '{}S'.format(n)
    elif parameter == 'long':
        if n <= 90:
            return '{}E'.format(n)
        return '{}W'.format(n)

def print_latlong(json_result:'json')->None:
    '''Takes a parsed JSON response and prints the latitude and longitude'''
    coord = json_result['route']['boundingBox']
    start_lat = abs(coord['lr']['lat'])
    start_long = abs(coord['lr']['lng'])
    print(map_direction('lat', start_lat), map_direction('long', start_long))
    end_lat = abs(coord['ul']['lat'])
    end_long = abs(coord['ul']['lng'])
    print(map_direction('lat', end_lat), map_direction('long', end_long))
    
    
    
            
