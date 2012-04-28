from time import sleep

from flask import Blueprint, session, redirect, url_for

from mouse import mousemove, mouseclick
import utils

iplayer = Blueprint('iplayer', __name__)

mediaweb_config = {
        'blueprint': iplayer,
        'title': 'iPlayer',
        'buttons': (
            ('Start playing', '/send_click'),
            ('Play/pause', '/iplayer_pauseplay'),
            ('Reload page', '/safari_reload'),
            ('Send escape', '/escape_key'),
            ),
        }

@iplayer.route('/send_click')
def send_click():
    _send_click()
    session['msg'] = "Send click to location of Bigscreen play area."
    return redirect(url_for('index'))

@iplayer.route('/iplayer_pauseplay')
def iplayer_pauseplay():
    _iplayer_pauseplay()
    session['msg'] = "Hit pause/play button."
    return redirect(url_for('index'))

@iplayer.route('/escape_key')
def escape_key():
    _escape_key()
    session['msg'] = "Sent Safari the Escape key."
    return redirect(url_for('index'))

@iplayer.route('/safari_reload')
def safari_reload():
    _safari_reload()
    session['msg'] = "Safari asked to reload the page."
    return redirect(url_for('index'))


# The controls

def _send_click():
    if not utils.is_running("Safari"): return
    width, height = utils.screen_size()
    cmd = """
    tell application "Safari" 
        activate
        set bounds of window 1 to {0, 22, 700, 800}
    end tell
    """ % locals()

    # These need to be done synchronously
    utils.execute_as_async(cmd)
    sleep(0.5)
    mouseclick(200, 420)
    sleep(0.5)
    mouseclick(200, 420)

def _iplayer_pauseplay():
    if not utils.is_running("Safari"): return
    width, height = utils.screen_size()
    mouseclick(30, height-50)
    sleep(1)
    mousemove(300,100)

def _safari_reload():
    if not utils.is_running("Safari"): return
    cmd = """
    tell application "Safari"
        activate
        tell application "System Events" to (keystroke "r" using {command down})
    end tell
    """ % locals()
    utils.execute_as(cmd)

def _escape_key():
    if not utils.is_running("Safari"): return
    cmd = """
    tell application "Safari"
        activate
        tell application "System Events" to key code 53
    end tell
    """ % locals()
    utils.execute_as(cmd)
