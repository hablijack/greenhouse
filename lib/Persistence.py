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

    def get_all_temperature_values(self):
        result = self.client.query('select value from temperature;')

    def get_all_humidity_values(self):
        result = self.client.query('select value from humidity;')

    def get_all_co2_values(self):
        result = self.client.query('select value from co2;')

    def get_all_brightness_values(self):
        result = self.client.query('select value from brightness;')

    def get_all_soil_moisture_values(self):
        result = self.client.query('select value from soil_moisture')

    def get_current_values(self):
        return {
            "temperature": self.__get_current_temperature_value(),
            "humidity": self.__get_current_humidity_value(),
            "co2": self.__get_current_co2_value(),
            "brightness": self.__get_current_brightness_value(),
            "soil_moisture": self.__get_current_soil_moisture_value()
        }

    def __get_current_temperature_value(self):
        results = self.client.query('select LAST("value") from temperature;')
        resultsInList = list(results.get_points(measurement='temperature'))
        return resultsInList[0]['last']

    def __get_current_humidity_value(self):
        results = self.client.query('select LAST("value") from humidity;')
        resultsInList = list(results.get_points(measurement='humidity'))
        return resultsInList[0]['last']

    def __get_current_co2_value(self):
        results = self.client.query('select LAST("value") from co2;')
        resultsInList = list(results.get_points(measurement='co2'))
        return resultsInList[0]['last']

    def __get_current_brightness_value(self):
        results = self.client.query('select LAST("value") from brightness;')
        resultsInList = list(results.get_points(measurement='brightness'))
        return resultsInList[0]['last']

    def __get_current_soil_moisture_value(self):
        results = self.client.query('select LAST("value") from soil_moisture')
        resultsInList = list(results.get_points(measurement='soil_moisture'))
        return resultsInList[0]['last']

    def set_scheduler(self, scheduler):
        self.scheduler = scheduler
