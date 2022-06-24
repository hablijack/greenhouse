# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
import os

""""
Represents the properties file and gives access to configuration options
"""


class Configuration:

    def __init__(self):
        self.config = configparser.ConfigParser()
        thisfolder = os.path.dirname(os.path.abspath(__file__))
        self.config.read(os.path.join(thisfolder, '../config.properties'))

    def server_port(self):
        return int(self.config.get('APPLICATION', 'port'))

    def barbara_pwd(self):
        return self.config.get('USER', 'barbara_pwd')

    def christoph_pwd(self):
        return self.config.get('USER', 'christoph_pwd')

    def greenhouse_satelite_host(self):
        return self.config.get('GREENHOUSE_SATELITE', 'host')

    def greenhouse_satelite_fan_relais(self):
        return self.config.get('GREENHOUSE_SATELITE', 'fan_relais')

    def greenhouse_satelite_plant_light_relais(self):
        return self.config.get('GREENHOUSE_SATELITE', 'plant_light_relais')
