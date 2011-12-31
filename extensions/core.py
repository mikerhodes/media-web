from flask import Blueprint, session, redirect, request, url_for

import utils

core = Blueprint('mediaweb_core', __name__)

mediaweb_config = {
        'blueprint': core,
        'title': 'Open & close',
        'buttons': (
            ('Open Plex', '/open_app?app=Plex'),
            ('Close Plex', '/quit_app?app=Plex'),

            ('Open Safari', '/open_app?app=Safari'),
            ('Close Safari', '/quit_app?app=Safari'),

            ('Open DVD Player', '/open_dvdplayer'),
            ('Close DVD Player', '/quit_app?app=DVD Player'),
            ),
        }

# Web-facing methods

@core.route("/open_url")
def open_url():
    url = request.args['url']
    url = utils.transform_url(url)

    _quit_app("Plex")
    _open_url_in_safari(url)
    session['msg'] = "Opened on TV! (You'll need to click Play, unfortunately)"
    return redirect(url_for('index'))

@core.route("/quit_app")
def quit_app():
    app_name = request.args['app']
    _quit_app(app_name)
    session['msg'] = "%(app_name)s asked to quit." % locals()
    return redirect(url_for('index'))

@core.route("/open_app")
def open_app():
    app_name = request.args['app']
    _open_app(app_name)
    session['msg'] = "%(app_name)s asked to open." % locals()
    return redirect(url_for('index'))

@core.route('/open_dvdplayer')
def open_dvdplayer():
    _open_dvdplayer()
    session['msg'] = "DVD Player asked to open and go full screen."
    return redirect(url_for('index'))


# The controls

def _quit_app(app_name):
    cmd = """
    if application "%(app_name)s" is running
        tell application "%(app_name)s" to quit
    end if
    """ % locals()
    utils.execute_as(cmd)

def _open_app(app_name):
    cmd = """
    tell application "%(app_name)s" 
        activate
    end tell
    """ % locals()
    utils.execute_as(cmd)

def _open_dvdplayer():
    cmd = """
    tell application "DVD Player"
        activate
        set viewer full screen to true
        play dvd
    end tell
    """
    utils.execute_as(cmd)

def _open_url_in_safari(url):
    width, height = utils.screen_size()
    cmd = """
    tell application "Safari"
        open location "%(url)s"
    end tell
    """ % locals()
    utils.execute_as(cmd)

