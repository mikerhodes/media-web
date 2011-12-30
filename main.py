from socket import gethostname
import os
import sys

from flask import Flask, render_template, session

import utils

extensions = []

app = Flask(__name__)
app.secret_key = 'Njminqche9vugWutU3HVsJQKAB'

# Load all extensions, which define the available buttons
for root, dirs, files in os.walk('extensions'):
    for name in files:
        if name.endswith(".py") and not name.startswith("__"):
            path = os.path.join(root, name)
            modulename = path.rsplit('.', 1)[0].replace('/', '.')
            __import__(modulename)
            module = sys.modules[modulename]
            config = module.mediaweb_config
            app.register_blueprint(config['blueprint'])

            extensions.append(config)

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
            extensions=extensions,
            )


if __name__ == "__main__":
    app.run(
            host='0.0.0.0', 
            port=PORT,
            #debug='Pro' in HOST,
            debug=True,
            )


