from socket import gethostname

import utils

from flask import Flask, request, render_template, session, redirect, url_for

import controls
import utils

app = Flask(__name__)
app.secret_key = 'Njminqche9vugWutU3HVsJQKAB'

PORT = 8080
HOST = gethostname()

@app.route("/")
def index():
    msg = session.pop('msg', None)
    return render_template(
            'index.html',
            host=HOST,
            port=PORT,
            status=msg,
            screen=utils.screen_size(),
            )

@app.route("/open_url")
def open_url():
    url = request.args['url']
    url = utils.transform_url(url)

    controls.quit_app("Plex")
    controls.open_url_in_safari(url)
    session['msg'] = "Opened on TV! (You'll need to click Play, unfortunately)"
    return redirect(url_for('index'))

@app.route("/quit_app")
def quit_app():
    app_name = request.args['app']
    controls.quit_app(app_name)
    session['msg'] = "%(app_name)s asked to quit." % locals()
    return redirect(url_for('index'))

@app.route("/open_app")
def open_app():
    app_name = request.args['app']
    controls.open_app(app_name)
    session['msg'] = "%(app_name)s asked to open." % locals()
    return redirect(url_for('index'))

@app.route("/sleep")
def sleep():
    controls.sleep_mac()
    session['msg'] = "Going to sleep!"
    return redirect(url_for('index'))

@app.route("/reboot")
def reboot():
    controls.reboot_mac()
    session['msg'] = "Rebooting!"
    return redirect(url_for('index'))

@app.route('/send_click')
def send_click():
    controls.send_click()
    session['msg'] = "Send click to location of Bigscreen play area."
    return redirect(url_for('index'))

@app.route('/iplayer_pauseplay')
def iplayer_pauseplay():
    controls.iplayer_pauseplay()
    session['msg'] = "Hit pause/play button."
    return redirect(url_for('index'))

@app.route('/itunes_playpause')
def itunes_playpause():
    controls.itunes_playpause()
    session['msg'] = "Hit pause/play button."
    return redirect(url_for('index'))

@app.route('/safari_reload')
def safari_reload():
    controls.safari_reload()
    session['msg'] = "Safari asked to reload the page."
    return redirect(url_for('index'))

@app.route('/escape_key')
def escape_key():
    controls.escape_key()
    session['msg'] = "Sent Safari the Escape key."
    return redirect(url_for('index'))

@app.route('/open_dvdplayer')
def open_dvdplayer():
    controls.open_dvdplayer()
    session['msg'] = "DVD Player asked to open and go full screen."
    return redirect(url_for('index'))

@app.route('/eject_disc')
def eject_disc():
    controls.eject_disc()
    session['msg'] = "Asked for DVD to be ejected."
    return redirect(url_for('index'))

@app.route('/move_mouse')
def move_mouse():
    controls.move_mouse()
    session['msg'] = "Mouse moved, screen should wake."
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(
            host='0.0.0.0', 
            port=PORT,
            #debug='Pro' in HOST,
            debug=True,
            )


