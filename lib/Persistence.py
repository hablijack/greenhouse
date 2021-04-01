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

    def get_air_temperature_inside_history(self):
        results = self.client.query(
            'select * from air_temp_inside ORDER BY time DESC')
        measurements = list(results.get_points())
        result_list = []
        for measurement in measurements:
            result_list.append(
                {'t': measurement['time'], 'y': measurement['value']})
        return result_list

    def get_air_temperature_outside_history(self):
        results = self.client.query(
            'select * from air_temp_outside ORDER BY time DESC')
        measurements = list(results.get_points())
        result_list = []
        for measurement in measurements:
            result_list.append(
                {'t': measurement['time'], 'y': measurement['value']})
        return result_list

    def get_short_history(self):
        results = self.client.query(
            'select * from /.*/ ORDER BY time DESC LIMIT 2')
        result_list = list(results.get_points())
        sorted_results = sorted(
            result_list, key=lambda x: x['time'], reverse=True)
        return sorted_results

    def __get_current_battery_capacity_value(self):
        results = self.client.query(
            'select LAST("value") from battery_capacity;')
        resultsInList = list(results.get_points(
            measurement='battery_capacity'))
        if not resultsInList:
            return None
        else:
            return resultsInList[0]['last']

    def get_current_values(self):
        return {
            "air_temp_inside": self.__get_current_air_temp_inside_value(),
            "light_inside": self.__get_current_light_inside_value(),
            "humidity_inside": self.__get_current_humidity_inside_value(),
            "soil_temp_inside": self.__get_current_soil_temp_inside_value(),
            "air_temp_outside": self.__get_current_air_temp_outside_value(),
            "co2_inside": self.__get_current_co2_inside_value(),
            "battery_capacity": self.__get_current_battery_capacity_value(),
            "wifi_strength": self.__get_current_wifi_strength_value()
        }

    def __get_current_wifi_strength_value(self):
        results = self.client.query('select LAST("value") from wifi_strength;')
        resultsInList = list(results.get_points(measurement='wifi_strength'))
        if not resultsInList:
            return None
        else:
            return resultsInList[0]['last']

    def __get_current_co2_inside_value(self):
        results = self.client.query('select LAST("value") from co2_inside;')
        resultsInList = list(results.get_points(measurement='co2_inside'))
        if not resultsInList:
            return None
        else:
            return resultsInList[0]['last']

    def __get_current_light_inside_value(self):
        results = self.client.query('select LAST("value") from light_inside;')
        resultsInList = list(results.get_points(measurement='light_inside'))
        if not resultsInList:
            return None
        else:
            return resultsInList[0]['last']

    def __get_current_air_temp_inside_value(self):
        results = self.client.query(
            'select LAST("value") from air_temp_inside;')
        resultsInList = list(results.get_points(measurement='air_temp_inside'))
        if not resultsInList:
            return None
        else:
            return resultsInList[0]['last']

    def __get_current_humidity_inside_value(self):
        results = self.client.query(
            'select LAST("value") from humidity_inside')
        resultsInList = list(results.get_points(measurement='humidity_inside'))
        if not resultsInList:
            return None
        else:
            return resultsInList[0]['last']

    def __get_current_air_temp_outside_value(self):
        results = self.client.query(
            'select LAST("value") from air_temp_outside')
        resultsInList = list(results.get_points(
            measurement='air_temp_outside'))
        if not resultsInList:
            return None
        else:
            return resultsInList[0]['last']

    def __get_current_soil_temp_inside_value(self):
        results = self.client.query(
            'select LAST("value") from soil_temp_inside')
        resultsInList = list(results.get_points(
            measurement='soil_temp_inside'))
        if not resultsInList:
            return None
        else:
            return resultsInList[0]['last']

    def set_scheduler(self, scheduler):
        self.scheduler = scheduler
