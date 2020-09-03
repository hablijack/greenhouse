#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from waitress import serve
from flask import Flask, request, render_template, Response, send_from_directory, jsonify
from lib.Persistence import Persistence
from lib.Scheduler import Scheduler
from datetime import datetime
import dateutil.parser
from flask import jsonify
from datetime import date

app = Flask(__name__)

@app.template_filter('iso8601_to_readable')
def iso8601_to_readable(value):
    return dateutil.parser.parse(value).strftime('%H:%M:%S')

@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('assets', path)

@app.route('/')
def overview():
    current = persistence.get_current_values()
    short_history = persistence.get_short_history()
    return render_template('index.html', current=current, short_history=short_history)

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/history/air_temperature_inside')
def air_temperature_inside():
    return jsonify(persistence.get_air_temperature_inside_history())

@app.route('/history/air_temperature_outside')
def air_temperature_outside():
    return jsonify(persistence.get_air_temperature_inside_history())

if __name__ == '__main__':
    persistence = Persistence()
    scheduler = Scheduler(persistence)
    serve(app, port=3000)
