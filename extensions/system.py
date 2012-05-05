from flask import Blueprint, session, redirect, url_for
from subprocess import Popen
from random import randint

import json

from mouse import mousemove

system = Blueprint('mediaweb_system', __name__)

mediaweb_config = {
        'blueprint': system,
        'title': 'System',
        'id': 'system',
        'buttons': (
            ('Sleep Mac', '/sleep'),
            ('Reboot Mac', '/reboot'),
            ('Move mouse', '/move_mouse'),
            ('Eject disc', '/eject_disc'),
            ),
        }

# Web-facing methods

@system.route("/sleep")
def sleep():
    _sleep_mac()
    result = dict()
    result['msg'] = "Going to sleep!"
    return json.dumps(result)

@system.route("/reboot")
def reboot():
    _reboot_mac()
    result = dict()
    result['msg'] = "Rebooting!"
    return json.dumps(result)

@system.route('/eject_disc')
def eject_disc():
    _eject_disc()
    result = dict()
    result['msg'] = "Asked for DVD to be ejected."
    return json.dumps(result)

@system.route('/move_mouse')
def move_mouse():
    _move_mouse()
    result = dict()
    result['msg'] = "Mouse moved, screen should wake."
    return json.dumps(result)


# The commands

def _sleep_mac():
    aplcmd = 'tell app "Finder" to sleep'
    cmd = "sleep 3 && /usr/bin/osascript -e '%(aplcmd)s'"
    Popen(cmd % locals(), shell=True)

def _reboot_mac():
    aplcmd = 'tell app "Finder" to restart'
    cmd = "sleep 3 && /usr/bin/osascript -e '%(aplcmd)s'"
    Popen(cmd % locals(), shell=True)

def _eject_disc():
    cmd = "drutil eject"
    Popen(cmd % locals(), shell=True)

def _move_mouse():
    # We need to move not always to the same spot
    # as otherwise it's not spotted as a move.
    mousemove(
            randint(200,300),
            randint(200,300),
            )

