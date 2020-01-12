#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from waitress import serve
from flask import Flask, request, render_template, Response, send_from_directory, jsonify
from lib.Persistence import Persistence
from lib.Scheduler import Scheduler

app = Flask(__name__)

@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('assets', path)

@app.route('/')
def overview():
    current = persistence.get_current_values()
    return render_template('index.html', current=current)

if __name__ == '__main__':
    persistence = Persistence()
    scheduler = Scheduler(persistence)
    serve(app, port=3000)
