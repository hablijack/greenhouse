#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import atexit
import random
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from lib.sensors.HumidityAndTemperature import HumidityAndTemperature
from lib.sensors.Light import Light
from lib.sensors.Battery import Battery
from lib.sensors.SoilTempInside import SoilTempInside
from lib.sensors.AirTempOutside import AirTempOutside
from lib.sensors.Gas import Gas
from lib.MagnetValves import MagnetValves
from lib.PlantLight import PlantLight


class Scheduler:

    def __init__(self, persistence):
        self.persistence = persistence
        self.scheduler = BackgroundScheduler()
        atexit.register(lambda: self.scheduler.shutdown())

        self.scheduler.add_job(
            id='measure_gas_sensor',
            func=self.measure_gas_sensor,
            trigger='interval',
            minutes=10)

        self.scheduler.add_job(
            id='measure_battery_state',
            func=self.measure_battery_state,
            trigger='interval',
            minutes=15)

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
            id='measure_air_temp_outside_sensor',
            func=self.measure_air_temp_outside_sensor,
            trigger='interval',
            minutes=10)

        self.scheduler.add_job(
            id='measure_soil_temp_inside_sensor',
            func=self.measure_soil_temp_inside_sensor,
            trigger='interval',
            minutes=10)

        self.scheduler.add_job(
            id='start_watering',
            func=self.start_watering1,
            trigger='cron',
            year='*',
            month='*',
            day='*',
            hour='8-10,17-19',
            minute='*/30',
            second=0)

        self.scheduler.add_job(
            id='stop_watering',
            func=self.stop_watering1,
            trigger='cron',
            year='*',
            month='*',
            day='*',
            hour='8-11,17-20',
            minute='*/33',
            second=0)

        self.scheduler.start()
        self.measure_all_values()

    def persist(self, timestamp, key, value):
        json_body = [{
            "measurement": key,
            "time": timestamp,
            "fields": {"value": value, "sensor": key}
        }]
        self.persistence.write(json_body)

    def start_watering1(self):
        MagnetValves().switch(1, True)

    def stop_watering1(self):
        MagnetValves().switch(1, False)

    def measure_battery_state(self):
        values = Battery().read()
        if values['battery_voltage']:
            self.persist(datetime.now(), 'battery_voltage',
                         values['battery_voltage'])
        if values['power_consumption']:
            self.persist(datetime.now(), 'power_consumption',
                         values['power_consumption'])
        if values['battery_capacity']:
            self.persist(datetime.now(), 'battery_capacity',
                         values['battery_capacity'])

    def measure_dht_sensor(self):
        values = HumidityAndTemperature().read()
        if values['temperature']:
            self.persist(datetime.now(), 'air_temp_inside',
                         values['temperature'])
        if values['humidity']:
            self.persist(datetime.now(), 'humidity_inside', values['humidity'])

    def measure_gas_sensor(self):
        value = Gas().read()
        if value:
            self.persist(datetime.now(), 'co2_inside', value)

    def measure_air_temp_outside_sensor(self):
        value = AirTempOutside().read()
        if value:
            self.persist(datetime.now(), 'air_temp_outside', value)

    def measure_soil_temp_inside_sensor(self):
        value = SoilTempInside().read()
        if value:
            self.persist(datetime.now(), 'soil_temp_inside', value)

    def measure_light_sensor(self):
        value = Light().read()
        if value:
            self.persist(datetime.now(), 'light_inside', value)

    def measure_all_values(self):
        MagnetValves().initialize()
        PlantLight().initialize()
        self.measure_dht_sensor()
        self.measure_light_sensor()
        self.measure_air_temp_outside_sensor()
        self.measure_soil_temp_inside_sensor()
        self.measure_battery_state()
        self.measure_gas_sensor()
