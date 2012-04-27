Media-web: simple media mac webserver
=====================================

Media-web is a web server designed to provide access to 
simple controls of a media centre mac:

- Open and close apps.
- Load a URL in Safari from a bookmarklet.
- Play/pause iTunes and iPlayer (in Safari).
- Sleep/reboot your mac.
- Exit screen saver by moving mouse.

And a few other bits.


Requirements
------------

- Python 2.6 or above (only tested with 2.6)
- Media-web uses the [Flask](http://flask.pocoo.org/) web framework.
- Most in-built commands are mac-specific.


Installation
------------

You need to:

- Install dependencies.
- Update config.py for your setup.

To install dependencies, it's best to set up a virtualenv for the app. I'd suggest
*not* using the --no-site-packages option.

Into this virtualenv, install flask.

You need to add the Quartz python bindings to your path. You do this by adding 
a .pth file to the virtualenv's site-packages folder:

    $ vim lib/python2.7/site-packages/coregraphics.pth

Into this file, just put a single line:

    /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/PyObjC

Save and quit. Obviously both of these lines need changing if you are not
using Python 2.7.

Next, you need to update config.py:

Add an entry to the screen_resolution stanza with your screen resolution.
Remove the examples if you want.

The name you use depends on your hostname, the code used to
choose the resolution to use is roughly (see utils.py):

    from socket import gethostname
    hostname = gethostname().lower()

    from config import screen_resolution
    for k,v in screen_resolution.items():
        if k in hostname:
            return v

Running the app
---------------

To run the app, run `python main.py` using the python install containing Flask.

Starting at startup
-------------------

Firstly, it seems like virtualenv python and starting at startup don't mix. At
least an hours frustration indicates this. So just use `easy_install flask` to
install flask into your system python.

To start `media-web` at startup, you need to add an entry to your system's
LaunchAgents. These are stored in `~/Library/LaunchAgents/`. Create a file
containing:

    CTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
        <key>Label</key>
        <string>uk.co.dx13.mediaweb</string>
        <key>KeepAlive</key>
        <true/>
        <key>RunAtLoad</key>
        <true/>
        <key>ProgramArguments</key>
        <array>
            <string>python</string>
            <string>/path/to/media-web/main.py</string>
        </array>
    </dict>
    </plist>



