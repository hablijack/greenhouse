##!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import board
import busio
import adafruit_veml7700


class Light():

    i2c = busio.I2C(board.SCL, board.SDA)
    VEML_SENSOR = adafruit_veml7700.VEML7700(i2c)

    def read(self):
        self.VEML_SENSOR.light_gain = self.VEML_SENSOR.ALS_GAIN_1_8
        self.VEML_SENSOR.light_integration_time = self.VEML_SENSOR.ALS_25MS
        return self.VEML_SENSOR.lux
