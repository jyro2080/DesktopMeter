import ctypes
import os
from time import sleep

xlib = None
try:
	xlib = ctypes.cdll.LoadLibrary( 'libX11.so.6')
except OSError:
	print "Could not load libX11.so.6"
	print "Idle time tracking will not be functional"

xss = None
try:
	if xlib != None:
		xss = ctypes.cdll.LoadLibrary( 'libXss.so.1')
except OSError:
	print "Could not load libXss.so.1"
	print "Idle time tracking will not be functional"

if xlib != None and xss != None:
	xlib_dpy = xlib.XOpenDisplay( os.environ['DISPLAY'])
	xlib_root = xlib.XDefaultRootWindow( xlib_dpy)

# Used for getting idle time
class XScreenSaverInfo( ctypes.Structure):
  """ typedef struct { ... } XScreenSaverInfo; """
  _fields_ = [('window',      ctypes.c_ulong), # screen saver window
              ('state',       ctypes.c_int),   # off,on,disabled
              ('kind',        ctypes.c_int),   # blanked,internal,external
              ('since',       ctypes.c_ulong), # milliseconds
              ('idle',        ctypes.c_ulong), # milliseconds
              ('event_mask',  ctypes.c_ulong)] # events

def get_idle_time():
    if xlib == None or xss == None:
        return 0
    xss.XScreenSaverAllocInfo.restype = ctypes.POINTER(XScreenSaverInfo)
    xss_info = xss.XScreenSaverAllocInfo()
    xss.XScreenSaverQueryInfo( xlib_dpy, xlib_root, xss_info)
    return xss_info.contents.idle / 1000


