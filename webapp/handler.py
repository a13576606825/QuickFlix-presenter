#!/usr/local/bin/python
# -*- coding: utf-8 -*-
"""
App
~~~

The Flask's `app` instance is initialized in this module.

Currently, the configuration is simple. We don't need to set any custom configuration
to Flask.
"""

import logging

from flask import jsonify, request, redirect, Response, render_template, url_for

from app import app

log = logging.getLogger(__name__)

@app.route('/', methods=["GET"])
def hello_world():
	return redirect('/home')

@app.route('/home', methods=["GET"])
def show_homepage():
	data = {}
	return render_template('home.html', **data)
