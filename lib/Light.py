# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO


class Light():

    def initialize(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(13, GPIO.OUT)
        GPIO.output(13, GPIO.HIGH)
        GPIO.cleanup()

    def switch(self, state):
        try:
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(13, GPIO.OUT)
            if state:
                GPIO.output(13, GPIO.LOW)
            else:
                GPIO.output(13, GPIO.HIGH)
                GPIO.cleanup()
        except RuntimeError as error:
            return None
