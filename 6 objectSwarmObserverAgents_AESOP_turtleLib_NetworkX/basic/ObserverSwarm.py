#ObserverSwarm.py
from ModelSwarm import *
from Tools import *
from Agent import *
from ActionGroup import *
from oActions import *
from Pen import *
import penPosition
import graphicDisplayGlobalVarAndFunctions as gvf
from parameters import *
import commonVar as common
import os

cycle=1

class ObserverSwarm:

    # creation step
    def __init__(self, project0):
        global project
        project=project0
        self.v_=[]
        self.n_=[]
        penPosition.setPen(self)
        
    # create objects
    def buildObjects(self):
        global cycle
        cycle=1

        loadParameters(self) #a function, to which we pass self

        self.conclude=False

        self.modelSwarm = ModelSwarm(self.nAgents,
                           self.worldXSize, self.worldYSize, project)
        self.modelSwarm.buildObjects()


    # actions
    def buildActions(self):

        global project
        print "#### Project", project,"starting."     
        print

        observerActions=open("./"+project+"/observerActions.txt")
        self.actionList=observerActions.read().split()
        #print self.actionList
        observerActions.close()

        self.modelSwarm.buildActions()

        # clock, do not remove or move from here; the position in
        # list can be also different
        self.actionGroup1 = ActionGroup ("clock")
        def do1(address, nCycles, actionList):
            global cycle
            cycle+=1 #the clock running
            print "Time =%2d" % cycle
            if cycle>nCycles:
                 insertElementNextPosition(actionList,"end")
        self.actionGroup1.do = do1 # do is a variable linking a method

        self.actionGroup1b = ActionGroup ("visualizeNet")
        self.actionGroup1b.do = do1b # do is a variable linking a method
    
        self.actionGroup2a = ActionGroup ("ask_all")
        self.actionGroup2a.do = do2a # do is a variable linking a method
    
        self.actionGroup2b = ActionGroup ("ask_one")
        self.actionGroup2b.do = do2b # do is a variable linking a method

        # previous steps, if empty, are defined in the specific
        # oAction.py file
        # do the same for new or different steps

        # do not remove or move from here and do not rename
        self.actionGroup3 = ActionGroup ("end")
        def do3(address):
            self.conclude=True
        self.actionGroup3.do = do3 # do is a variable linking a method

        

    # run
    def run(self):
        global cycle
        print "Time =%2d" % cycle

        if self.nCycles==0: print "The # of required cycles is 0. "
        while not self.conclude and self.nCycles>0:
            
            localEventList=self.actionList[:]   

            while len(localEventList)>0 and not self.conclude:
                subStep=extractASubStep(localEventList)

                found=False

                if subStep == "modelStep":
                    found=True
                    self.modelSwarm.step(cycle)
                    # in a reasonable way, the model makes a step before
                    # that the observer looks at the effects of model actions
 
                if subStep == "clock":
                    found=True
                    self.actionGroup1.do(self, self.nCycles, localEventList)
                    # self here is the model env.
                    # not added automatically
                    # being do a variable

                if subStep == "visualizeNet":
                    found=True
                    self.actionGroup1b.do(self)  
 
                if subStep == "ask_all":
                    found=True
                    self.actionGroup2a.do(self, cycle)

                if subStep == "ask_one":
                    found=True
                    self.actionGroup2b.do(self, cycle)

                if subStep == "pause":
                    found=True
                    raw_input ("Hit enter key to continue")   

                if subStep == "prune":
                    found=True
                    common.prune=True
                    newValue=raw_input (("Prune links with weight < %d\n"+\
                                         "Enter to confirm "+\
                                         "or introduce a new level: ") % \
                                          common.pruneThreshold)
                    if newValue !="": common.pruneThreshold=int(newValue)

                if subStep == "end":
                    found=True
                    self.actionGroup3.do(self)
                    raw_input("enter to conclude")
                    # look at graphicDisplayGlobalVarAndFunctions.py in the
                    # folder of the project
                    gvf.closeNetworkXdisplay()

                if not found: print "Warning: step %s not found" % subStep
                    
        if self.modelSwarm.getFile() != "": self.modelSwarm.getFile().close()
