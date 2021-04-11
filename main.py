#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from waitress import serve
from flask import Flask, request, render_template, Response, send_from_directory, jsonify
from lib.Persistence import Persistence
from lib.Scheduler import Scheduler
from datetime import datetime
import dateutil.parser
from flask import jsonify
from datetime import date
from lib.MagnetValves import MagnetValves
from lib.PlantLight import PlantLight

app = Flask(__name__)


@app.template_filter('iso8601_to_readable')
def iso8601_to_readable(value):
    return dateutil.parser.parse(value).strftime('%H:%M:%S')

@app.template_filter('air_inside_status')
def air_inside_status(value):
    cssClass = 'green'
    if(value < 6):
        cssClass='red'
    elif(value >= 6):
        cssClass='orange'
    elif(value > 20):
        cssClass='green'
    elif(value > 30):
        cssClass='red'
    return cssClass

@app.template_filter('air_outside_status')
def air_outside_status(value):
    cssClass = 'green'
    if(value < 6):
        cssClass='red'
    elif(value >= 6):
        cssClass='orange'
    elif(value > 15):
        cssClass='green'
    elif(value > 30):
        cssClass='red'
    return cssClass

@app.template_filter('soil_temp_status')
def soil_temp_status(value):
    cssClass = 'green'
    if(value < 4):
        cssClass='red'
    elif(value >= 4):
        cssClass='orange'
    elif(value >= 13):
        cssClass='green'
    elif(value > 29):
        cssClass='red'
    return cssClass

@app.template_filter('light_status')
def light_status(value):
    cssClass = 'green'
    if(value < 400):
        cssClass='red'
    elif(value >= 400):
        cssClass='orange'
    elif(value >= 5000):
        cssClass='green'
    return cssClass


@app.template_filter('humidity_status')
def humidity_status(value):
    cssClass = 'green'
    if(value < 50):
        cssClass='red'
    elif(value >= 50):
        cssClass='orange'
    elif(value >= 65):
        cssClass='green'
    return cssClass

@app.template_filter('co2_status')
def co2_status(value):
    cssClass = 'green'
    if(value < 400):
        cssClass='red'
    elif(value >= 400):
        cssClass='orange'
    elif(value >= 600):
        cssClass='green'
    elif(value >= 2000):
        cssClass='red'
    return cssClass

@app.template_filter('soil_status')
def soil_status(value):
    cssClass = 'green'
    if(value < 10):
        cssClass='red'
    elif(value >= 10):
        cssClass='orange'
    elif(value >= 50):
        cssClass='green'
    return cssClass

@app.template_filter('battery_status')
def battery_status(value):
    cssClass = 'green'
    if(value < 30):
        cssClass='red'
    elif(value >= 30):
        cssClass='orange'
    elif(value >= 50):
        cssClass='green'
    return cssClass

@app.template_filter('wifi_status')
def wifi_status(value):
    cssClass = 'green'
    if(value < 35):
        cssClass='red'
    elif(value >= 35):
        cssClass='orange'
    elif(value >= 45):
        cssClass='green'
    return cssClass

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'assets/img/favicons'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('assets', path)


@app.route('/')
def overview():
    current = persistence.get_current_values()
    short_history = persistence.get_short_history()
    return render_template('index.html', current=current, short_history=short_history)


@app.route('/control')
def control():
    return render_template('control.html')


@app.route('/history')
def history():
    return render_template('history.html')


@app.route('/history/air_temperature_inside')
def air_temperature_inside():
    timefilter = request.args.get('timefilter')
    return jsonify(persistence.get_history_for(timefilter, 'air_temp_inside'))


@app.route('/history/air_temperature_outside')
def air_temperature_outside():
    timefilter = request.args.get('timefilter')
    return jsonify(persistence.get_history_for(timefilter, 'air_temp_outside'))


@app.route('/history/wifi_strength')
def wifi_strength():
    timefilter = request.args.get('timefilter')
    return jsonify(persistence.get_history_for(timefilter, 'wifi_strength'))


@app.route('/history/battery_capacity')
def battery_capacity():
    timefilter = request.args.get('timefilter')
    return jsonify(persistence.get_history_for(timefilter, 'battery_capacity'))


@app.route('/history/co2')
def co2():
    timefilter = request.args.get('timefilter')
    return jsonify(persistence.get_history_for(timefilter, 'co2_inside'))


@app.route('/history/brightness')
def brightness():
    timefilter = request.args.get('timefilter')
    return jsonify(persistence.get_history_for(timefilter, 'light_inside'))


@app.route('/history/humidity')
def humidity():
    timefilter = request.args.get('timefilter')
    return jsonify(persistence.get_history_for(timefilter, 'humidity_inside'))


@app.route('/control/relay', methods=['POST'])
def control_relay():
    identifier = request.form.get('identifier')
    state = request.form.get('state')
    if identifier == 'light':
        PlantLight().switch(state == 'true')
    elif identifier == 'vent1':
        MagnetValves().switch(1, (state == 'true'))
    elif identifier == 'vent2':
        MagnetValves().switch(2, (state == 'true'))
    elif identifier == 'vent3':
        MagnetValves().switch(3, (state == 'true'))
    return jsonify({'state': 'OK'})


if __name__ == '__main__':
    persistence = Persistence()
    scheduler = Scheduler(persistence)
    serve(app, port=3000)
