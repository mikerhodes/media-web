from flask import Blueprint, session, redirect, url_for

import controls

itunes = Blueprint('mediaweb_itunes', __name__)

mediaweb_config = {
        'blueprint': itunes,
        'title': 'iTunes',
        'buttons': (
            ('Play/pause', '/itunes_playpause'),
            ),
        }

@itunes.route('/itunes_playpause')
def itunes_playpause():
    controls.itunes_playpause()
    session['msg'] = "Hit pause/play button."
    return redirect(url_for('index'))
