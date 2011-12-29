import os
from time import sleep
import subprocess
from subprocess import Popen

from mouse import mousemove, mouseclick

import utils


def sleep_mac():
    aplcmd = 'tell app "Finder" to sleep'
    cmd = "sleep 3 && /usr/bin/osascript -e '%(aplcmd)s'"
    Popen(cmd % locals(), shell=True)

def reboot_mac():
    aplcmd = 'tell app "Finder" to restart'
    cmd = "sleep 3 && /usr/bin/osascript -e '%(aplcmd)s'"
    Popen(cmd % locals(), shell=True)


def quit_app(app_name):
    cmd = """osascript<<END
    if application "%(app_name)s" is running
        tell application "%(app_name)s" to quit
    end if
    END"""
    Popen(cmd % locals(), shell=True)


def open_app(app_name):
    cmd = """osascript<<END
    tell application "%(app_name)s" 
        activate
    end tell
    END"""
    Popen(cmd % locals(), shell=True)

def open_dvdplayer():
    cmd = """osascript<<END
    tell application "DVD Player"
        activate
        set viewer full screen to true
        play dvd
    end tell
    END"""
    Popen(cmd % locals(), shell=True)

def open_url_in_safari(url):
    width, height = utils.screen_size()
    cmd = """osascript<<END
    tell application "Safari"
        open location "%(url)s"
    end tell
    END"""
    Popen(cmd % locals(), shell=True)

def send_click():
    if not is_running("Safari"): return
    width, height = utils.screen_size()
    cmd = """osascript<<END
    tell application "Safari" 
        activate
        set bounds of window 1 to {0, 22, 700, 800}
    end tell
    END"""

    # These need to be done synchronously
    os.system(cmd % locals())
    sleep(0.5)
    mouseclick(200, 360)
    sleep(0.5)
    mouseclick(200, 360)

def iplayer_pauseplay():
    if not is_running("Safari"): return
    width, height = utils.screen_size()
    mouseclick(30, height-50)
    sleep(1)
    mousemove(300,100)

def safari_reload():
    if not is_running("Safari"): return
    cmd = """osascript<<END
    tell application "Safari"
        activate
        tell application "System Events" to (keystroke "r" using {command down})
    end tell
    END"""
    Popen(cmd % locals(), shell=True)

def escape_key():
    if not is_running("Safari"): return
    cmd = """osascript<<END
    tell application "Safari"
        activate
        tell application "System Events" to key code 53
    end tell
    END"""
    Popen(cmd % locals(), shell=True)

def eject_disc():
    cmd = "drutil eject"
    Popen(cmd % locals(), shell=True)

def move_mouse():
    mousemove(300,100)


def is_running(app_name):
    return True
    cmd = """osascript -e 'tell application "%(app_name)s" to return running'"""

    #result = subprocess.check_output(cmd, shell=True) # 2.7 only

    process = Popen(cmd % locals(), shell=True)
    result,err = process.communicate()

    return "true" in result

def itunes_playpause():
    cmd = """osascript<<END
    tell application "iTunes"
        playpause
    end tell
    END"""
    Popen(cmd % locals(), shell=True)
    






