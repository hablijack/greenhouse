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
        try:
            return self.VEML_SENSOR.light
        except RuntimeError as error:
            return None
