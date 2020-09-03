#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import atexit
import random
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from lib.sensors.HumidityAndTemperature import HumidityAndTemperature
from lib.sensors.Light import Light
from lib.sensors.Battery import Battery
from lib.Display import Display


class Scheduler:

    def __init__(self, persistence):
        self.persistence = persistence
        self.scheduler = BackgroundScheduler()
        atexit.register(lambda: self.scheduler.shutdown())

        self.scheduler.add_job(
            id='measure_battery_state',
            func=self.measure_battery_state,
            trigger='interval',
            minutes=10)

        self.scheduler.add_job(
            id='measure_dht_sensor',
            func=self.measure_dht_sensor,
            trigger='interval',
            minutes=10)

        self.scheduler.add_job(
            id='measure_light_sensor',
            func=self.measure_light_sensor,
            trigger='interval',
            minutes=5)

        self.scheduler.add_job(
            id='update_display_stats',
            func=self.update_display_stats,
            trigger='interval',
            minutes=1)

        self.scheduler.start()
        self.measure_all_values()
        self.update_display_stats()

    def persist(self, timestamp, key, value):
        json_body = [{
            "measurement": key,
            "time": timestamp,
            "fields": { "value": value, "sensor": key }
        }]
        self.persistence.write(json_body)

    def update_display_stats(self):
        values = self.persistence.get_current_values()
        Display().render(values)

    def measure_battery_state(self):
        values = Battery().read()
        if values['voltage']:
            self.persist(datetime.now(), 'voltage', values['voltage'])
        if values['battery_power']:
            self.persist(datetime.now(), 'battery_power', values['battery_power'])
        if values['battery_capacity']:
            self.persist(datetime.now(), 'battery_capacity', values['battery_capacity'])

    def measure_dht_sensor(self):
        values = HumidityAndTemperature().read()
        if values['temperature']:
            self.persist(datetime.now(), 'air_temp_inside', values['temperature'])
        if values['humidity']:
            self.persist(datetime.now(), 'humidity_inside', values['humidity'])

    def measure_light_sensor(self):
        value = Light().read()
        if value:
            self.persist(datetime.now(), 'light_inside', value)

    def measure_all_values(self):
        self.measure_dht_sensor()
        self.measure_light_sensor()
        self.measure_battery_state()
