# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from lib.Configuration import Configuration


class Fan():

    def switch(self, state):
        r = requests.post(
            Configuration().greenhouse_satelite_host() + '/relais/set',
            json={Configuration().greenhouse_satelite_fan_relais(): state}
        )

    def state(self, state):
        r = requests.get(
            url=Configuration().greenhouse_satelite_host() + '/relais/state'
        )
        relaisState = r.json()
        return relaisState[Configuration().greenhouse_satelite_fan_relais()]
