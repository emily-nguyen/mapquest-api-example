# Project 3: MapQuest API Example User Interface

import mapquest_parse

def main():
    APP_KEY = 'Fmjtd%7Cluu82luanl%2C72%3Do5-948x04'
    URL = 'http://open.mapquestapi.com/directions/v2/route?key={}&'.format(APP_KEY)
    
    inputs = int(input())
    location_list = input_list(inputs)
    outputs = int(input())
    output_list = input_list(outputs)

    for i in range(len(location_list)-1):
        url = mapquest_parse.format_url(URL, location_list[i], location_list[i+1])
        print(url)
        print()
        mapquest_parse.download_url(url)

def input_list(n:int)->list:
    '''Returns a list of n locations taken in as input'''
    result = []
    for i in range(n):
        x = input()
        result.append(x)
    return result 
        
if __name__ == '__main__':
    main() 
