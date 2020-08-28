#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from influxdb import InfluxDBClient

class Persistence:

    def __init__(self):
        self.client = InfluxDBClient(
            host='yggdrasil.fritz.box',
            port=8086,
            username='greenhouse',
            password='greenhouse',
            database='greenhouse')
        self.client.create_database('greenhouse')

    def write(self, json_data):
        self.client.write_points(json_data)

    def get_short_history(self):
        results = self.client.query('select * from /.*/ ORDER BY time DESC LIMIT 3')
        result_list = list(results.get_points())
        sorted_results = sorted(result_list, key=lambda x: x['time'], reverse=True)
        return sorted_results

    def get_current_values(self):
        return {
            "air_temp_inside": self.__get_current_air_temp_inside_value(),
            "light_inside": self.__get_current_light_inside_value(),
            "humidity_inside": self.__get_current_humidity_inside_value()
        }

    def __get_current_light_inside_value(self):
        results = self.client.query('select LAST("value") from light_inside;')
        resultsInList = list(results.get_points(measurement='light_inside'))
        if not resultsInList:
            return None
        else:
            return resultsInList[0]['last']

    def __get_current_air_temp_inside_value(self):
        results = self.client.query('select LAST("value") from air_temp_inside;')
        resultsInList = list(results.get_points(measurement='air_temp_inside'))
        if not resultsInList:
            return None
        else:
            return resultsInList[0]['last']

    def __get_current_humidity_value(self):
        results = self.client.query('select LAST("value") from humidity_inside')
        resultsInList = list(results.get_points(measurement='humidity_inside'))
        if not resultsInList:
            return None
        else:
            return resultsInList[0]['last']

    def set_scheduler(self, scheduler):
        self.scheduler = scheduler
