#from Quartz import CGDisplayBounds
#from Quartz import CGMainDisplayID

from socket import gethostname
from config import screen_resolution

from subprocess import Popen
import os

def execute_as(applescript):
    cmd = """osascript<<END
        %s
    END""" % applescript
    Popen(cmd, shell=True)

def execute_as_async(applescript):
    cmd = """osascript<<END
        %s
    END""" % applescript
    os.system(cmd)


hostname = gethostname().lower()

def transform_url(url):
    """We transform some URLs, e.g., iPlayer -> BigScreen"""

    #"http://www.bbc.co.uk/iplayer/episode/b017h80m" --->
    #"http://www.bbc.co.uk/iplayer/bigscreen/tv/episode/b017h80m/"

    if "www.bbc.co.uk/iplayer/episode" in url:
        return url.replace(
                "www.bbc.co.uk/iplayer/episode", 
                "www.bbc.co.uk/iplayer/bigscreen/tv/episode")

    return url

def screen_size():
    #mainMonitor = CGDisplayBounds(CGMainDisplayID())
    #return (mainMonitor.size.width, mainMonitor.size.height)

    # I can't automatically seem to get this reliably for my purposes
    for k,v in screen_resolution.items():
        if k in hostname:
            return v


def is_running(app_name):
    return True
    cmd = """osascript -e 'tell application "%(app_name)s" to return running'"""

    #result = subprocess.check_output(cmd, shell=True) # 2.7 only

    process = Popen(cmd % locals(), shell=True)
    result,err = process.communicate()

    return "true" in result
