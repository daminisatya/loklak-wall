import os,binascii
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, Blueprint, Response
from flask import send_from_directory
from flask.ext.responses import json_response, xml_response, auto_response
import datetime, chartkick
import json
from pprint import pprint
import logging
from loklak import Loklak
from collections import Counter
import requests
import time

from config import *

app = Flask(__name__)
ck = Blueprint('ck_page', __name__, static_folder=chartkick.js(), static_url_path='/static')
app.register_blueprint(ck, url_prefix='/ck')
app.jinja_env.add_extension("chartkick.ext.charts")

@app.route('/yield')
def yieldFun():
    def inner():
        l = Loklak()
        tweets = l.search('fossasia')
        # for tweet in tweets['statuses']:
        #     time.sleep(1)                           # Don't need this just shows the text streaming
        #     yield tweet.text
        for i in range(0,10000):
        	yield i
    return flask.Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show th$

@app.route('/ajax/wall/<query>', methods=['GET'])
def ajaxwall(query=None):
	q = query
	l = Loklak()
	tweets = l.search(q)
	for tweet in tweets['statuses']:
		try:
			imageUrl = tweet['user']['profile_image_url_https']
			newUrl = imageUrl.split('_bigger')
			updatedUrl = newUrl[0]+newUrl[1]
			tweet['user']['profile_image_url_https'] = updatedUrl
		except:
			pass
	return json_response(tweets)

@app.route('/wall/<query>', methods=['GET'])
def wall(query=None):
	q = query
	l = Loklak()
	tweets = l.search(q)
	for tweet in tweets['statuses']:
		try:
			imageUrl = tweet['user']['profile_image_url_https']
			newUrl = imageUrl.split('_bigger')
			updatedUrl = newUrl[0]+newUrl[1]
			tweet['user']['profile_image_url_https'] = updatedUrl
		except:
			pass
	return render_template('index.html', name=q, tweets=tweets, BASE_URL=BASE_URL)


@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.secret_key=os.urandom(24)
    # app.permanent_session_lifetime = datetime.timedelta(seconds=200)
    app.run('0.0.0.0',port=5000)
