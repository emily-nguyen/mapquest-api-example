# Project 3: MapQuest API Example Parse JSON

import http.client
import urllib.request
import urllib.error
import urllib.parse 

def format_url(base_url:str, start_loc:str, end_loc:str)->str:
    '''Takes in a start and end location and returns a url string formatted
    with the inputs'''
    url_encode = urllib.parse.urlencode([('from', start_loc), ('to', end_loc)])
    return (base_url + url_encode)
    

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
