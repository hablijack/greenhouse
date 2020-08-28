##!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import board
import adafruit_dht

class Humidity():

    def read(self):
        humidity = None
        while humidity == None:
            try:
                dhtDevice = adafruit_dht.DHT22(board.D26)
                humidity = dhtDevice.humidity
                dhtDevice.exit()
            except RuntimeError as error:
                # Errors happen fairly often, 
                # DHT's are hard to read, 
                # just keep going
                time.sleep(2.0)
                continue
        return humidity
