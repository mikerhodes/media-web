from time import sleep
import json

from flask import Blueprint, session, redirect, url_for

from mouse import mousemove, mouseclick
import utils

plugin_4od = Blueprint('4od', __name__)

mediaweb_config = {
        'blueprint': plugin_4od,
        'title': '4od',
        'id': '4od',
        'buttons': (
            ('Start playing fullscreen', '/4od_start'),
            ('Play/pause', '/4od_pauseplay'),
            ('Parental guidance accept', '/4od_pg_accept'),
            # From the iPlayer plugin...
            ('Enter fullscreen', '/4od_fullscreen'),
            ('Leave fullscreen', '/escape_key'),
            ('Reload page', '/safari_reload'),
            ('Close Safari', '/quit_safari'),
            ),
        }

@plugin_4od.route('/4od_start')
def fourod_start():
    _fourod_start()
    result = dict()
    result['msg'] = "Send click to location of Bigscreen play area."
    return json.dumps(result)

@plugin_4od.route('/4od_pg_accept')
def fourod_pg_accept():
    _fourod_pg_accept()
    result = dict()
    result['msg'] = "Send click to location of Bigscreen play area."
    return json.dumps(result)

@plugin_4od.route('/4od_fullscreen')
def fourod_fullscreen():
    _fourod_fullscreen()
    result = dict()
    result['msg'] = "Send click to location of Bigscreen play area."
    return json.dumps(result)

@plugin_4od.route('/4od_pauseplay')
def fourod_pauseplay():
    _fourod_pauseplay()
    result = dict()
    result['msg'] = "Hit pause/play button."
    return json.dumps(result)


# The controls

def _fourod_start():
    if not utils.is_running("Safari"): return
    width, height = utils.screen_size()
    cmd = """
    tell application "Safari" 
        activate
        set bounds of window 1 to {0, 22, 1000, 8000}
    end tell
    """ % locals()

    # These need to be done synchronously
    utils.execute_as_async(cmd)
    # full screen
    sleep(0.5)
    mouseclick(850, 700)

    # play
    sleep(1)
    #mouseclick(550, 500)
    mouseclick(width/2, height/2)

def _fourod_pg_accept():
    if not utils.is_running("Safari"): return
    width, height = utils.screen_size()
    #cmd = """
    #tell application "Safari" 
        #activate
        #set bounds of window 1 to {0, 22, 1000, 8000}
    #end tell
    #""" % locals()

    ## These need to be done synchronously
    #utils.execute_as_async(cmd)
    #sleep(0.5)
    mouseclick(width * 0.40, height * 0.59)

def _fourod_fullscreen():
    if not utils.is_running("Safari"): return
    width, height = utils.screen_size()
    cmd = """
    tell application "Safari" 
        activate
        set bounds of window 1 to {0, 22, 1000, 8000}
    end tell
    """ % locals()

    # These need to be done synchronously
    utils.execute_as_async(cmd)
    sleep(0.5)
    mouseclick(850, 700)
    #sleep(0.5)
    #mouseclick(200, 420)

def _fourod_pauseplay():
    if not utils.is_running("Safari"): return
    width, height = utils.screen_size()
    mouseclick(30, height-50)
    sleep(1)
    mousemove(300,100)

