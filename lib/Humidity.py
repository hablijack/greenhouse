##!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import board
import adafruit_dht

class Humidity():

    def read(self):
        dhtDevice = adafruit_dht.DHT22(board.D26)
        humidity = None
        while humidity == None:
            try:
                humidity = dhtDevice.humidity
            except RuntimeError as error:
                # Errors happen fairly often, DHT's are hard to read, just keep going
                print(error.args[0])
                time.sleep(2.0)
                continue
        return humidity
