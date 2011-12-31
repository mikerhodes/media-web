from flask import Blueprint, session, redirect, url_for
from subprocess import Popen

from mouse import mousemove

system = Blueprint('mediaweb_system', __name__)

mediaweb_config = {
        'blueprint': system,
        'title': 'System',
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
    session['msg'] = "Going to sleep!"
    return redirect(url_for('index'))

@system.route("/reboot")
def reboot():
    _reboot_mac()
    session['msg'] = "Rebooting!"
    return redirect(url_for('index'))

@system.route('/eject_disc')
def eject_disc():
    _eject_disc()
    session['msg'] = "Asked for DVD to be ejected."
    return redirect(url_for('index'))

@system.route('/move_mouse')
def move_mouse():
    _move_mouse()
    session['msg'] = "Mouse moved, screen should wake."
    return redirect(url_for('index'))


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
    mousemove(300,100)

