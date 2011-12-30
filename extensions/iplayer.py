from flask import Blueprint, session, redirect, url_for

import controls

iplayer = Blueprint('iplayer', __name__)

mediaweb_config = {
        'blueprint': iplayer,
        'title': 'iPlayer',
        'buttons': (
            ('Send click to play full screen', '/send_click'),
            ('Play/pause', '/iplayer_pauseplay'),
            ('Reload page', '/safari_reload'),
            ('Send escape', '/escape_key'),
            ),
        }

@iplayer.route('/send_click')
def send_click():
    controls.send_click()
    session['msg'] = "Send click to location of Bigscreen play area."
    return redirect(url_for('index'))

@iplayer.route('/iplayer_pauseplay')
def iplayer_pauseplay():
    controls.iplayer_pauseplay()
    session['msg'] = "Hit pause/play button."
    return redirect(url_for('index'))

@iplayer.route('/escape_key')
def escape_key():
    controls.escape_key()
    session['msg'] = "Sent Safari the Escape key."
    return redirect(url_for('index'))

@iplayer.route('/safari_reload')
def safari_reload():
    controls.safari_reload()
    session['msg'] = "Safari asked to reload the page."
    return redirect(url_for('index'))
