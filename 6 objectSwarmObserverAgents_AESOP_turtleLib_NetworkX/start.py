#start 6 objectSwarmObserverAgentsAESOP.py


# 'project' is by default both the name of the application and of the subfolder
# that contains its code; the subfolder is supposed to be placed within the
# SLAPP tree

# the folder can can be placed outside the SLAPP tree if we place a file
# project.txt in the folder "6 objectSwarmObserverAgents_AESOP_turtleLib_NetworkX"
# the file has to contain the path and the name of the folder of the project

print "SLAPP 0.95"
import os
confirm="n"
found=False
names=os.listdir("./")
if "project.txt" in names:
    currentProject=open ("project.txt","r")
    pathAndProject=currentProject.readline()
    if pathAndProject[-1]=="\n" or pathAndProject[-1]=="\r":
        pathAndProject=pathAndProject[0:-1]
    if pathAndProject[-1]=="\n" or pathAndProject[-1]=="\r":
        pathAndProject=pathAndProject[0:-1]
    # -1 means: last character
    # [0:-1] meand: the string but the last caracter
    # the last caracter is eliminated in the giben case (twice) to avoid
    # interferences between the control characters in the file and the
    # path definition
    print "path and project = " + pathAndProject
    confirm=raw_input("do you confirm? ([y]/n): ")
    if confirm == "y" or confirm == "Y" or confirm == "": found=True
    currentProject.close()

if confirm == "y" or confirm == "Y" or confirm == "":
    project = pathAndProject
else:
    project = raw_input("Project name? ")
    if not project in names: print "Project " + project + " not found"
    else:
        found=True
        project="./"+project



if found:
 import sys
 sys.path.append("./$$slapp$$")
 if confirm !="y": sys.path.append(project)
 else:             sys.path.append(pathAndProject)

 from Tools import *
 from ObserverSwarm import *
 import commonVar as common

 common.debug=False # if debug il True a large part of the try/except
                    # structures will be bypassed, so the errors will
                    # be managed directly by the Python interpreter

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
