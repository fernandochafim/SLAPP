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

(2015 06 10)

0.95 simplified the reference to agentList in Agent.py in production project

simplified Agent.py in projects using a superAgent class as a container of unspecific methods

(2015 08 08)

0.951 fixes a bug in the version control for the library NetworkX, in production/parameters.py

(2015 08 08)

0.952 fixes a residual bug in the version control for the library NetworkX, in production/parameters.py

(2015 08 20)

0.953 adds the capability of recognizing if running in IPython or in Python

(2015 08 26)

0.96  clarified scheduling in Observer.py about 'visualizeNet'; corrected also
oActions.py in production project; no changes in the results

(2015 08 31)

1.0   Having now a Handbook, this is version 1.0  

(2015 09 02)

1.01  Reorganized start.py in the folder '6 objectSwarmObserverAgents_AESOP_turtleLib_NetworkX' considering running SLAPP also in IPython

(2015 09 10)

1.1   New starting point in the main folder (runShell.py)

The file project.txt (look at the Reference Handbook) can be also placed in the main folder

Better management of 'end' condition for graphical projects

(2015 09 29)

1.11  Allowing a wider use of WorldState. This is only a temporary patch, the interface
to WorldState in ModelSwarm.py will be quite soon re-engineered, also having as
optional the presence of WorldState.py in the folder of a project

(2016 02 15)

1.2   Introducing the extension .txtx (extended txt) to be used for the definition
of the files describing the agents

Have a look to the Reference Handbook, section *The agents and their sets*, sub section *Files .txtx in defining the agents*

(2016 04 08)
1.2.1 Modifications facing v. 1.5.1 of matplotlib, mainly relevant with IPython and
%matplolib magics

new folder *matplotlib_aQuestForAFewGraphicCapabilities* to explore matplotlib in Python & IPython environments
