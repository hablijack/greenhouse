# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import gpiozero


class MagnetValves():

    def switch(self, valve_no, state):
        try:
            gpio = -1
            if valve_no == 1:
                gpio = 13
            elif valve_no == 2:
                gpio = 6
            elif valve_no == 3:
                gpio = 5
            relay = gpiozero.OutputDevice(
                gpio,
                active_high=True,
                initial_value=False
            )
            if state:
                relay.on()
            else:
                relay.off()
        except RuntimeError as error:
            return None
