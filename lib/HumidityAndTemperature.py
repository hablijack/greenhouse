##!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import board
import adafruit_dht

class HumidityAndTemperature():

    DHT_SENSOR = adafruit_dht.DHT22(board.D26)

    def read(self):
        temperature = None
        humidity = None
        while temperature == None and humidity == None:
            try:
                temperature = self.DHT_SENSOR.temperature
                humidity = self.DHT_SENSOR.humidity
            except RuntimeError as error:
                print(error)
                # Errors happen fairly often, 
                # DHT's are hard to read, 
                # just keep going
                time.sleep(2.0)
                continue
        print(temperature)
        return {'temperature': temperature, 'humidity': humidity}
