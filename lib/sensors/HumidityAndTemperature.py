##!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import time
#import board
#import adafruit_dht

#class HumidityAndTemperature():
#
#    def read(self):
#        temperature = None
#        humidity = None
#        while temperature == None and humidity == None:
#            try:
#                DHT_SENSOR = adafruit_dht.DHT22(board.D26)
#                temperature = DHT_SENSOR.temperature
#                humidity = DHT_SENSOR.humidity
#            except RuntimeError as error:
#                #print(error)
#                # Errors happen fairly often, 
#                # DHT's are hard to read, 
#                # just keep going
#                time.sleep(2.0)
#                continue
#        return {'temperature': temperature, 'humidity': humidity}

import Adafruit_DHT

class HumidityAndTemperature():
    def read(self):
        temperature = None
        humidity = None
        sensor = Adafruit_DHT.DHT22
        humidity, temperature = Adafruit_DHT.read_retry(sensor, 26)
        return {'temperature': temperature, 'humidity': humidity}

