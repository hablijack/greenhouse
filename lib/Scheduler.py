#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import atexit
import random
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

from lib.Humidity import Humidity
from lib.AirTempInside import AirTempInside


class Scheduler:

    def __init__(self, persistence):
        self.persistence = persistence
        self.scheduler = BackgroundScheduler()
        atexit.register(lambda: self.scheduler.shutdown())

        self.scheduler.add_job(
            id='measure_air_temp_inside',
            func=self.measure,
            args=[AirTempInside, 'air_temp_inside'],
            trigger='interval',
            seconds=60)

        self.scheduler.add_job(
            id='measure_humidity',
            func=self.measure,
            args=[Humidity, 'humidity'],
            trigger='interval',
            seconds=60)

        self.scheduler.start()
        self.measure_all_values()

    def persist(self, timestamp, key, value):
        json_body = [{
            "measurement": key,
            "time": timestamp,
            "fields": { "value": value, "sensor": key }
        }]
        self.persistence.write(json_body)

    def measure(self, sensor, id):
        value = sensor().read()
        if value != None:
            self.persist(datetime.now(), id, value)
        else: 
            print("ERROR: Could not read from " + id + " sensor!")

    def measure_all_values(self):
        self.measure(Humidity, 'humidity')
        self.measure(AirTempInside, 'air_temp_inside')
