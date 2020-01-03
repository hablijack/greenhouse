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
            id='measure_temperature',
            func=self.measure_temperature,
            trigger='interval',
            seconds=60)

        self.scheduler.add_job(
            id='measure_humidity',
            func=self.measure_humidity,
            trigger='interval',
            seconds=60)

        self.scheduler.add_job(
            id='measure_soil_moisture',
            func=self.measure_soil_moisture,
            trigger='interval',
            seconds=60)

        self.scheduler.add_job(
            id='measure_brightness',
            func=self.measure_brightness,
            trigger='interval',
            seconds=60)

        self.scheduler.add_job(
            id='measure_co2',
            func=self.measure_co2,
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

    def measure_temperature(self):
        print("... messe die Temperatur.")
        value = random.uniform(1, 30)
        self.persist(datetime.now(), 'temperature', value)

    def measure_humidity(self):
        print("... messe die Luftfeuchtigkeit.")
        value = random.uniform(1, 100)
        self.persist(datetime.now(), 'humidity', value)

    def measure_soil_moisture(self):
        print("... messe die Bodenfeuchte.")
        value = random.uniform(1, 100)
        self.persist(datetime.now(), 'soil_moisture', value)

    def measure_brightness(self):
        print("... messe die Helligkeit.")
        value = random.uniform(1, 30)
        self.persist(datetime.now(), 'brightness', value)

    def measure_co2(self):
        print("... messe die CO2 Konzentration.")
        value = random.uniform(1, 100)
        self.persist(datetime.now(), 'co2', value)
