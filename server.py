import os,binascii
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, Blueprint
from flask import send_from_directory
from flask.ext.responses import json_response, xml_response, auto_response
import datetime, chartkick
import json
from pprint import pprint
import logging
from loklak import Loklak
from collections import Counter
import requests

app = Flask(__name__)
ck = Blueprint('ck_page', __name__, static_folder=chartkick.js(), static_url_path='/static')
app.register_blueprint(ck, url_prefix='/ck')
app.jinja_env.add_extension("chartkick.ext.charts")

@app.route('/ajax/wall/<query>', methods=['GET'])
def ajaxwall(query=None):
	q = query
	l = Loklak()
	tweets = l.search(q)
	return json_response(tweets)

@app.route('/wall/<query>', methods=['GET'])
def wall(query=None):
	q = query
	l = Loklak()
	tweets = l.search(q)
	return render_template('index.html', name=q, tweets=tweets)


@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.secret_key=os.urandom(24)
    # app.permanent_session_lifetime = datetime.timedelta(seconds=200)
    app.run('0.0.0.0',port=5000)
