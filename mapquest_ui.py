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
            json_result = mapquest_parse.get_result(url)
            result.extend(i.generate(json_result))

        if type(i) == mapquest_classes.Steps:
            print('\nDIRECTIONS')
            for k in result:
                print(k)
        elif type(i) == mapquest_classes.Distance:
            print('\nTotal Distance: {} miles'.format(int(sum(result)+0.5)))
        elif type(i) == mapquest_classes.Time:
            print('\nTotal Time: {} minutes'.format(int(sum(result)/60+0.5)))
        elif type(i) == mapquest_classes.LatLong:
            print()
            for k in range(len(location_list)-2):
                result.pop(-(k+1))
            for c in result:
                print(c[0], c[1])
    
    print('\nDirections Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
            
def input_list(n:int)->list:
    '''Returns a list of n locations taken in as input'''
    result = []
    for i in range(n):
        x = input()
        result.append(x)
    return result
        
if __name__ == '__main__':
    main() 
