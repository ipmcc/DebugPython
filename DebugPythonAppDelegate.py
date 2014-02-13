from Foundation import *
from AppKit import *

class DebugPythonAppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        print "did finish launching"
    
    def applicationWillTerminate_(self,sender):
        print "will terminate"