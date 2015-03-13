# Project 3: MapQuest API Example Parse JSON

import http.client
import urllib.request
import urllib.error

APP_KEY = 'Fmjtd%7Cluu82luanl%2C72%3Do5-948x04'
URL = 'http://open.mapquestapi.com/directions/v2/route?key={}&from={}&to={}'

def format_location(location:str)->str:
    '''Takes a location and formats the string to make it valid'''
    string = ''
    loc = location.split()
    if len(loc) > 1:
        lst = loc[:-1]
        for i in lst:
            string += i + '+'
        return string + loc[-1]
    return location 

def format_url(start_loc:str, end_loc:str)->str:
    '''Takes in a start and end location and returns a url string formatted
    with the inputs'''
    start = format_location(start_loc)
    end = format_location(end_loc)
    return URL.format(APP_KEY, start, end)

def download_url(url:str)->None:
    '''Takes in a url and prints out the contents of the web page'''
    response = None
    try:
        response = urllib.request.urlopen(url)
        content = response.read()
        print(content)
    except urllib.error.HTTPError as e:
        print('Failed to download contents of URL')
        print('Status code: {}'.format(e.code))
        print()
    finally:
        if response != None:
            response.close()
