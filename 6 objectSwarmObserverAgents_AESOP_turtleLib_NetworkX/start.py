#start 6 objectSwarmObserverAgentsAESOP.py


# 'project' is both the name of the application and of the subfolder that
# contains it
project = raw_input("SLAPP 0.92\nProject name? ")

import os
names=os.listdir("./")
if not project in names: print "Project " + project + " not found"

else:
 import sys
 sys.path.append("./$$slapp$$")
 sys.path.append("./"+project)

 from Tools import *
 from ObserverSwarm import *
 import commonVar as common

 common.debug=True  # if debug il True all the try/excpt structures will be
                    # bypassed, so the errors will be managed directly
                    # by the Python interpreter

                    # this choice can be useful when you build a new project
                    # and as an expert user you want to check the errors
                    # in a basic way
 print "debug =",common.debug

 observerSwarm = ObserverSwarm(project)

 # create objects
 observerSwarm.buildObjects()

 # create actions
 observerSwarm.buildActions()

 # run
 observerSwarm.run()
