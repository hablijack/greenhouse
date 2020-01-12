#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import Adafruit_DHT

class Humidity():

    def read(self):
        DHT_TYPE = Adafruit_DHT.AM2302
        DHT_PIN  = 23
        humidity, temperature = Adafruit_DHT.read_retry(DHT_TYPE, DHT_PIN)
        return humidity