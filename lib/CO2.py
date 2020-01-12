#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import busio
import adafruit_ccs811
import board

class CO2():

    def read(self):
        i2c_bus = busio.I2C(board.SCL, board.SDA)
        ccs =  adafruit_ccs811.CCS811(i2c_bus)
        return ccs.eco2bb