# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import gpiozero


class Light():

    def switch(self, state):
        try:
            relay = gpiozero.OutputDevice(
                19,
                active_high=True,
                initial_value=False
            )
            if state:
                relay.on()
            else:
                relay.off()
        except RuntimeError as error:
            return None
