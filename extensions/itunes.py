from flask import Blueprint, session, redirect, url_for

import utils

itunes = Blueprint('mediaweb_itunes', __name__)

mediaweb_config = {
        'blueprint': itunes,
        'title': 'iTunes',
        'id': 'itunes',
        'buttons': (
            ('Play/pause', '/itunes_playpause'),
            ),
        }

@itunes.route('/itunes_playpause')
def itunes_playpause():
    _itunes_playpause()
    session['msg'] = "Hit pause/play button."
    return redirect(url_for('index'))

def _itunes_playpause():
    cmd = """
    tell application "iTunes"
        playpause
    end tell
    """ % locals()
    utils.execute_as(cmd)
