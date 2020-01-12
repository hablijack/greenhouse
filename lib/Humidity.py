#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import board
import adafruit_dht

class Humidity():

    def read(self):
        dhtDevice = adafruit_dht.DHT22(board.D18)
        humidity = dhtDevice.humidity
        return humidity