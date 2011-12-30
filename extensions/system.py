from flask import Blueprint, session, redirect, url_for

import controls

system = Blueprint('mediaweb_system', __name__)

mediaweb_config = {
        'blueprint': system,
        'title': 'System',
        'buttons': (
            ('Sleep Mac', '/sleep'),
            ('Reboot Mac', '/reboot'),
            ('Move mouse', '/eject_disc'),
            ('Eject disc', '/move_mouse'),
            ),
        }

@system.route("/sleep")
def sleep():
    controls.sleep_mac()
    session['msg'] = "Going to sleep!"
    return redirect(url_for('index'))

@system.route("/reboot")
def reboot():
    controls.reboot_mac()
    session['msg'] = "Rebooting!"
    return redirect(url_for('index'))

@system.route('/eject_disc')
def eject_disc():
    controls.eject_disc()
    session['msg'] = "Asked for DVD to be ejected."
    return redirect(url_for('index'))

@system.route('/move_mouse')
def move_mouse():
    controls.move_mouse()
    session['msg'] = "Mouse moved, screen should wake."
    return redirect(url_for('index'))

