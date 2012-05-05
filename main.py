from socket import gethostname
import os
import sys

from flask import Flask, render_template, session

# Test config.py exists
try:
    import config
    config.screen_resolution
except ImportError:
    print "ERROR: no config set"
    print "Please copy config.py.example to config.py and customise."
    sys.exit(1)
except AttributeError, ex:
    print "ERROR: config has required attribute missing - see config.py.example."
    print ex.args
    sys.exit(1)

import utils

extensions = []

app = Flask(__name__)
app.secret_key = 'Njminqche9vugWutU3HVsJQKAB'

# Load all extensions, which define the available buttons
my_path = os.path.dirname(os.path.realpath(__file__))
extensions_path = os.path.join(my_path, 'extensions')
for root, dirs, files in os.walk(extensions_path):
    for name in files:
        if name.endswith(".py") and not name.startswith("__"):
            path = os.path.join(root, name)
            modulename = 'extensions.' + name.rsplit('.', 1)[0]
            __import__(modulename)
            module = sys.modules[modulename]
            m_config = module.mediaweb_config
            app.register_blueprint(m_config['blueprint'])

            extensions.append(m_config)

            extensions.sort(key=lambda x: config.order.index(x['id']))

PORT = 8080
HOST = gethostname()

@app.route("/old")
def old():
    msg = session.pop('msg', None)
    return render_template(
            'index.html',
            host=HOST,
            port=PORT,
            status=msg,
            screen=utils.screen_size(),
            extensions=extensions,
            )

@app.route("/")
def index():
    msg = session.pop('msg', None)
    return render_template(
            'jqm.html',
            host=HOST.split('.')[0],
            port=PORT,
            status=msg,
            screen=utils.screen_size(),
            extensions=extensions,
            )

import pybonjour


def register_callback(sdRef, flags, errorCode, name, regtype, domain):
    if errorCode == pybonjour.kDNSServiceErr_NoError:
        print 'Registered service:'
        print '  name    =', name
        print '  regtype =', regtype
        print '  domain  =', domain


if __name__ == "__main__":
    #name = "media-web@%s" % HOST
    #regtype= "_http._tcp"
    #sdRef = pybonjour.DNSServiceRegister(name=name,
                                         #regtype=regtype,
                                         #port=PORT,
                                         #callBack=register_callback)
    #pybonjour.DNSServiceProcessResult(sdRef)

    try:
        app.run(
                host='0.0.0.0', 
                port=PORT,
                #debug='Pro' in HOST,
                debug=True,
                )
    except KeyboardInterrupt:
        #print "Deregistering with bonjour"
        #sdRef.close()
        #pybonjour.DNSServiceRefDeallocate(sdRef)
        pass


