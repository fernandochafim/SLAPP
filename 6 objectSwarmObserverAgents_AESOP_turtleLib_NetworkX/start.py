#start 6 objectSwarmObserverAgentsAESOP.py


# 'project' is both the name of the application and of the subfolder that
# contains it
project = raw_input("SLAPP 0.9\nProject name? ")

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

 observerSwarm = ObserverSwarm(project)

 # create objects
 observerSwarm.buildObjects()

 # create actions
 observerSwarm.buildActions()

 # run
 observerSwarm.run()
