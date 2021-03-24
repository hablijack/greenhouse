##!/usr/bin/env python3
# -*- coding: utf-8 -*-

import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


class SoilMoisture():

    i2c = busio.I2C(board.SCL, board.SDA)

    def read(self):
        ads = ADS.ADS1115(self.i2c)
        chan1 = AnalogIn(ads, ADS.P1)
        print(chan1.value, chan1.voltage)


