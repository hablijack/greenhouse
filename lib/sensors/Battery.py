##!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import board
import adafruit_ina260


class Battery():

    i2c = board.I2C()
    INA260_SENSOR = adafruit_ina260.INA260(i2c)

    def convert_voltage_to_percent(self, voltage):
        if voltage > 12.6:
            return 100
        elif voltage >= 12.5:
            return 90
        elif voltage >= 12.42:
            return 80
        elif voltage >= 12.32:
            return 70
        elif voltage >= 12.2:
            return 60
        elif voltage >= 12.06:
            return 50
        elif voltage >= 11.9:
            return 40
        elif voltage >= 11.75:
            return 30
        elif voltage >= 11.58:
            return 20
        elif voltage >= 11.31:
            return 10
        elif voltage <= 10.5:
            return 0

    def read(self):   
        try:
            voltage = self.INA260_SENSOR.voltage
            return {
                'battery_voltage': voltage, 
                'power_consumption': self.INA260_SENSOR.power,
                'battery_capacity': self.convert_voltage_to_percent(voltage)
            }
        except RuntimeError as error:
            return None
