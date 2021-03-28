# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO


class MagnetValves():


    def initialize(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup([19,5,6], GPIO.OUT)
        GPIO.output([19,5,6], GPIO.HIGH)
        GPIO.cleanup()


    def switch(self, valve_no, state):
        try:
            gpiopin = -1
            if valve_no == 1:
                gpiopin = 19
            elif valve_no == 2:
                gpiopin = 5
            elif valve_no == 3:
                gpiopin = 6
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(gpiopin, GPIO.OUT)
            if state:
                GPIO.output(gpiopin, GPIO.LOW)
            else:
                GPIO.output(gpiopin, GPIO.HIGH)
                GPIO.cleanup()
        except RuntimeError as error:
            return None
