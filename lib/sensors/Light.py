##!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import board
import busio
import adafruit_veml7700

# 0.3	Full moon on a clear night
# 50	Family living room lights (Australia, 1998) – This is pretty dark in my opinion
# 80	Office building hallway lighting
# 320–500	Office lighting
# 400	Sunrise or Sunset on a clear day
# 1000	Overcast day (Same light they use in a studio)
# 10,000–25,000	Full daylight (but not direct sun)
# 32,000–100,000	Direct Sunlight
# 
# Low light plants
# Lux 500-2500			
#
# Medium light plants
# Lux 2500-10000
#
# Bright light plants
# Lux 10000-20000
#
# Very bright light plants
# Lux 20000-50000


class Light():

    i2c = busio.I2C(board.SCL, board.SDA)
    VEML_SENSOR = adafruit_veml7700.VEML7700(i2c)

    def read(self):   
        try:
            return self.VEML_SENSOR.lux
        except RuntimeError as error:
            return None
