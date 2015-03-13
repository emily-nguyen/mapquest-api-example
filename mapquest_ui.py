# Project 3: MapQuest API Example User Interface

import mapquest_parse
import mapquest_classes

def main():

    inputs = int(input())
    location_list = input_list(inputs)
    outputs = int(input())
    output_list = input_list(outputs)

    classes = [] 
    for i in output_list:
        if i == 'STEPS':
            classes.append(mapquest_classes.Steps())
        elif i == 'TOTALDISTANCE':
            classes.append(mapquest_classes.Distance())
        elif i == 'TOTALTIME':
            classes.append(mapquest_classes.Time())
        elif i == 'LATLONG':
            classes.append(mapquest_classes.LatLong())

    for i in classes:
        result = [] 
        for j in range(len(location_list)-1):
            url = mapquest_parse.format_url(location_list[j], location_list[j+1])
            print(url)
            print()
            json_result = mapquest_parse.get_result(url)
            result.extend(i.generate(json_result))
        for k in result:
            print(k)

def input_list(n:int)->list:
    '''Returns a list of n locations taken in as input'''
    result = []
    for i in range(n):
        x = input()
        result.append(x)
    return result
        
if __name__ == '__main__':
    main() 
