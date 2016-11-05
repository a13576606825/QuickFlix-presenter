#!/usr/local/bin/python
# -*- coding: utf-8 -*-
"""
Handler:  defined end points
~~~

"""

import logging
from flask import jsonify, request, redirect, Response, render_template, url_for

from app import app
import core

log = logging.getLogger(__name__)

@app.route('/', methods=["GET"])
def hello_world():
	return redirect('/home')

@app.route('/home', methods=["GET"])
def show_homepage():
	data = {}
	return render_template('home.html', **data)

@app.route('/result', methods=["GET"])
def show_result():
	query = request.args.get('query').strip()
	log.info(query)
	isBlur, rankedMovieTitles = core.blur_match(query)
	topTitle = rankedMovieTitles[0]['title'] if len(rankedMovieTitles) > 0 else None
	results = core.retrieveResult(topTitle)

	movie_info = core.retrieve_movie_info(topTitle)
	data = {
		'movie_info':movie_info,
		'topTitle': topTitle,
		'query':query,
		'isBlur': isBlur,
		'rankedMovieTitles': rankedMovieTitles,
		'results': results,
	}
	return render_template('result.html', **data)
