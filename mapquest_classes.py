# Project 3: MapQuest API Example Classes

import mapquest_parse

class Steps:
    def generate(self, json_result:'json')->list:
        '''Returns a list of the directions / steps'''
        return mapquest_parse.parse_steps(json_result)

class Distance:
    def generate(self, json_result:'json')->int:
        '''Returns the total distance rounded to the nearest mile'''
        return mapquest_parse.parse_distance(json_result)

class Time:
    def generate(self, json_result:'json')->int:
        '''Returns the total time rounded to the nearest minute'''
        return mapquest_parse.parse_time(json_result)

class LatLong:
    def generate(self, json_result:'json')->list:
        '''Returns a list of the latitude and longitude'''
        return mapquest_parse.parse_latlong(json_result)
