#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import TCP_NODELAY
from influxdb import InfluxDBClient
from datetime import date, timedelta


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

    def get_history_for(self, timefilter, identifier):
        filter = self.__generate_influx_filter(timefilter)
        results = self.client.query(
            'select * from ' + identifier + filter)
        measurements = list(results.get_points())
        result_list = []
        for measurement in measurements:
            result_list.append(
                {'t': measurement['time'], 'y': measurement['value']})
        return result_list

    def __generate_influx_filter(self, timefilter):
        filter = " ORDER BY time DESC"
        if timefilter == 'today':
            today = date.today()
            tomorrow = date.today() + timedelta(days=1)
            filter = " where time >= '" + \
                today.strftime("%Y-%m-%d") + "' and time < '" + \
                tomorrow.strftime("%Y-%m-%d") + "'" + filter
        elif timefilter == 'week':
            tomorrow = date.today() + timedelta(days=1)
            firstOfWeek = date.today() - timedelta(days=7)
            filter = " where time >= '" + \
                firstOfWeek.strftime("%Y-%m-%d") + "' and time < '" + \
                tomorrow.strftime("%Y-%m-%d") + "'" + filter
        elif timefilter == 'month':
            tomorrow = date.today() + timedelta(days=1)
            firstOfMonth = date.today() - timedelta(days=30)
            filter = " where time >= '" + \
                firstOfMonth.strftime("%Y-%m-%d") + "' and time < '" + \
                tomorrow.strftime("%Y-%m-%d") + "'" + filter
        elif timefilter == 'year':
            tomorrow = date.today() + timedelta(days=1)
            firstOfYear = date.today() - timedelta(days=365)
            filter = " where time >= '" + \
                firstOfYear.strftime("%Y-%m-%d") + "' and time < '" + \
                tomorrow.strftime("%Y-%m-%d") + "'" + filter
        return filter

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
