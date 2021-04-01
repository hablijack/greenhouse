# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess


class Wifi():

    def read(self):
        try:
            cmd = subprocess.Popen(
                'iwconfig wlan0', shell=True, stdout=subprocess.PIPE)
            percent = 0
            for line in cmd.stdout:
                output = line.decode("utf-8")
                if 'Link Quality' in output:
                    strength = output.split(
                        '=')[1].split(' ')[0].split('/')
                    cur = int(strength[0])
                    max = int(strength[1])
                    percent = (cur/(max/100))
                    break
            return percent
        except RuntimeError as error:
            return None
