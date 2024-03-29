# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from lib.Configuration import Configuration


class PlantLight():

    def switch(self, state):
        r = requests.post(
            Configuration().greenhouse_satelite_host() + '/relais/set',
            json={Configuration().greenhouse_satelite_plant_light_relais(): state}
        )

    def state(self):
        r = requests.get(
            url=Configuration().greenhouse_satelite_host() + '/relais/state'
        )
        relaisState = r.json()
        return relaisState[Configuration().greenhouse_satelite_plant_light_relais()]
