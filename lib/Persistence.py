#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from influxdb import InfluxDBClient

class Persistence:

    def __init__(self):
        self.client = InfluxDBClient(
            host='localhost',
            port=8086,
            username='root',
            password='root',
            database='greenhouse')
        self.client.create_database('greenhouse')

    def write(self, json_data):
        self.client.write_points(json_data)

    def get_current_values(self):
        return {
            "temp_outside": self.__get_current_temp_outside_value(),
            "temp_inside": self.__get_current_temp_inside_value(),
            "soil_moisture_1": self.__get_current_soil_moisture_1_value(),
            "soil_moisture_2": self.__get_current_soil_moisture_2_value(),
            "co2": self.__get_current_co2_value(),
            "humidity": self.__get_current_humidity_value()
        }

    def __get_current_temp_inside_value(self):
        results = self.client.query('select LAST("value") from temp_inside;')
        resultsInList = list(results.get_points(measurement='temp_inside'))
        if not resultsInList:
            return None
        else:
            return resultsInList[0]['last']

    def __get_current_temp_outside_value(self):
        results = self.client.query('select LAST("value") from temp_outside;')
        resultsInList = list(results.get_points(measurement='temp_outside'))
        if not resultsInList:
            return None
        else:
            return resultsInList[0]['last']

    def __get_current_soil_moisture_1_value(self):
        results = self.client.query('select LAST("value") from soil_moisture_1')
        resultsInList = list(results.get_points(measurement='soil_moisture_1'))
        if not resultsInList:
            return None
        else:
            return resultsInList[0]['last']

    def __get_current_soil_moisture_2_value(self):
        results = self.client.query('select LAST("value") from soil_moisture_2')
        resultsInList = list(results.get_points(measurement='soil_moisture_2'))
        if not resultsInList:
            return None
        else:
            return resultsInList[0]['last']

    def __get_current_humidity_value(self):
        results = self.client.query('select LAST("value") from humidity')
        resultsInList = list(results.get_points(measurement='humidity'))
        if not resultsInList:
            return None
        else:
            return resultsInList[0]['last']

    def __get_current_co2_value(self):
        results = self.client.query('select LAST("value") from co2')
        resultsInList = list(results.get_points(measurement='co2'))
        if not resultsInList:
            return None
        else:
            return resultsInList[0]['last']

    def set_scheduler(self, scheduler):
        self.scheduler = scheduler
