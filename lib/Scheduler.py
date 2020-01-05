# -*- coding: utf-8 -*-
import atexit
import random
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

class Scheduler:

    def __init__(self, persistence):
        self.persistence = persistence
        self.scheduler = BackgroundScheduler()
        atexit.register(lambda: self.scheduler.shutdown())

        self.scheduler.add_job(
            id='measure_temp_inside',
            func=self.measure_temp_inside,
            trigger='interval',
            seconds=60)

        self.scheduler.add_job(
            id='measure_temp_outside',
            func=self.measure_temp_outside,
            trigger='interval',
            seconds=60)

        self.scheduler.add_job(
            id='measure_soil_moisture_1',
            func=self.measure_soil_moisture_1,
            trigger='interval',
            seconds=60)

        self.scheduler.add_job(
            id='measure_soil_moisture_2',
            func=self.measure_soil_moisture_2,
            trigger='interval',
            seconds=60)

        self.scheduler.start()

    def persist(self, timestamp, key, value):
        json_body = [{
            "measurement": key,
            "time": timestamp,
            "fields": { "value": value }
        }]
        self.persistence.write(json_body)

    def measure_temp_inside(self):
        value = random.uniform(1, 30)
        self.persist(datetime.now(), 'temp_inside', value)

    def measure_temp_outside(self):
        value = random.uniform(1, 30)
        self.persist(datetime.now(), 'temp_outside', value)

    def measure_soil_moisture_1(self):
        value = random.uniform(1, 100)
        self.persist(datetime.now(), 'soil_moisture_1', value)

    def measure_soil_moisture_2(self):
        value = random.uniform(1, 100)
        self.persist(datetime.now(), 'soil_moisture_2', value)

