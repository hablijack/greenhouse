##!/usr/bin/env python3
# -*- coding: utf-8 -*-

import busio
import adafruit_sgp30
import board

# < 300     : low
# 300 - 400 : normal
# > 400     : good
# > 1000    : too much


class Gas():

    i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
    sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

    def read(self):
        try:
            eCO2, TVOC = self.sgp30.iaq_measure()
            return eCO2
        except RuntimeException as ex:
            print(ex)
            return None
