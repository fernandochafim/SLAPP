(2015 December)
0.9     First version distributed via the Git system

(2015 02 11)
0.91    Eliminated unused file ObserverSwarm.py in folder
'6 objectSwarmObserverAgents_AESOP_turtleLib_NetworkX/basic'

(2015 03 01)

0.911   Improved the presentation with a quick introduction

(2015 04 10)

0.92 Introduced in folder 6, file start.py, a *debug* common variable; if set to True, a large part of the try/except structures will be bypassed, so the errors will be managed directly by the Python interpreter;  this choice can be useful when you build a new project and as an expert user you want to check the errors in a basic way

(2015 04 10)

0.921 Set, in start.py, common.debug=_False_ as default

(2015 04 21)

0.922 Modified ObserverSwarm.py correcting cycle => common.cycle to facilitate the access to this information in any part of the applications

(2015 04 24)

0.93 Added the project 'debug' to check debug capabilities. Have a look to the
file debug.txt in the folder 'debug' of folder '6 objectSwarmObserverAgents_AESOP_turtleLib_NetworkX'

Modified a few error message of ModelSwarm.py if the required method does not exist

Improved the Tools.py output in case of error on a method

(2015 06 07)

0.94 'project' is by default both the name of the application and of the subfolder
that contains its code; the subfolder is supposed to be placed within the
SLAPP tree

With this version, the folder can be placed outside the SLAPP tree
if we place a file project.txt in the folder
"6 objectSwarmObserverAgents_AESOP_turtleLib_NetworkX"

The file has to contain the path and the name of the folder of the project
