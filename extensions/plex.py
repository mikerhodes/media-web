from flask import Blueprint, session, redirect, url_for
from subprocess import Popen
from random import randint

import requests

import json

from mouse import mousemove

plex = Blueprint('mediaweb_plex', __name__)

mediaweb_config = {
        'blueprint': plex,
        'title': 'Plex',
        'id': 'plex',
        'buttons': (
            ('Refresh TV shows', '/plex_tv_refresh'),
            ('Refresh films', '/plex_film_refresh'),
            ),
        }

# Web-facing methods

@plex.route("/plex_tv_refresh")
def tv_refresh():
    result = dict()
    try:
        r = requests.get('http://localhost:32400/library/sections/2/refresh')
        success = r.status_code >= 200 and r.status_code < 300
        result['msg'] = 'Refreshing TV shows' if success else 'Error refreshing TV shows'
    except:
        result['msg'] = 'Error refreshing TV shows'
    return json.dumps(result)

@plex.route("/plex_film_refresh")
def film_refresh():
    result = dict()
    try:
        r = requests.get('http://localhost:32400/library/sections/1/refresh')
        success = r.status_code >= 200 and r.status_code < 300
        result['msg'] = 'Refreshing films' if success else 'Error refreshing films'
    except:
        result['msg'] = 'Error refreshing films'
    return json.dumps(result)

