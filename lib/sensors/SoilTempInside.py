##!/usr/bin/env python3
# -*- coding: utf-8 -*-


class SoilTempInside():

    SENSOR_FILE = '/sys/bus/w1/devices/28-800000014a00/w1_slave'

    def read(self):
        try:
            f = open(self.SENSOR_FILE, 'r')
            lines = f.readlines()
            f.close()
            while lines[0].strip()[-3:] != 'YES':
                time.sleep(0.2)
                lines = read_temp_raw()
            equals_pos = lines[1].find('t=')
            if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                temp_c = float(temp_string) / 1000.0
            else:
                temp_c = None
            return temp_c
        except RuntimeError as error:
            return None

