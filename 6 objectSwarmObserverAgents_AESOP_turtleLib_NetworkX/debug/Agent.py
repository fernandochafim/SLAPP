#Agent.py
from Tools import *
from agTools import *
import commonVar as common

class Agent(SuperAgent):
    def __init__(self, number,myWorldState,
                 xPos, yPos, lX =-20,rX=19, bY=-20,tY=19, agType=""):
        # the environment
        self.agOperatingSets=[]
        self.number = number
        self.lX = lX
        self.rX = rX
        self.bY = bY
        self.tY = tY
        self.myWorldState = myWorldState
        self.agType=agType
        # the agent
        self.xPos = xPos
        self.yPos = yPos
        print "agent", self.agType, "#", self.number, \
     	      "has been created at", self.xPos, ",", self.yPos


    # ",**d" in the parameter lists of the methods is a place holder
    # in case we use, calling the method, a dictionary as last par

    # check the clock
    def checkClock(self,**d):
        print "I'm %s agent # %d: " % (self.agType,self.number),
        print "clock is at ", common.cycle

    # check the superClock
    def checkSuperClock(self,**d):
        print "I'm %s agent # %d: " % (self.agType,self.number),
        print "clock is at ", common.cycles

    # the action, also jumping
    def randomMovement(self,**k):
        if random.random()<=self.myWorldState.getGeneralMovingProb():
            print "agent %s # %d moving" % (self.agType,self.number)
            self.jump=k["jump"]
            dx=randomMove(self.jump)
            self.xPos +=dx
            dy=randomMove(self.jump)
            self.yPos += dy
            #self.xPos = (self.xPos + self.worldXSize) % self.worldXSize
            #self.yPos = (self.yPos + self.worldYSize) % self.worldYSize
            if self.xPos < self.lX : self.xPos=self.lX
            if self.xPos > self.rX : self.xPos=self.rX
            if self.yPos < self.bY : self.yPos=self.bY
            if self.yPos > self.tY : self.yPos=self.tY

            if abs(dx) > 4 and abs(dy) > 4 :

            # modify actionGroup "move" via local code execution
                actionGroup=actionDictionary.get("move","none")
                                    # in case, return "none"

                if actionGroup=="none": print "warning, actionGroup not found "+\
                                "in agent "+ str(self.number)

                else:
                   # this code show that it is possibile to generate local code
                   # run by the askEachAgentInCollectionAndExecLocalCode
                   # structure in mActions.py
                   if int(self.number/2)*2 == self.number:
                         oddEven = "print 'my number is even'"
                   else: oddEven = "print 'my number is odd'"
                   setLocalCode("print 'agent %s # %d made a big jump';"\
                                           % (self.agType,self.number) +\
                                oddEven)


    # report
    def reportPosition(self,**d):
        print self.agType, "agent # ", self.number, " is at X = ", \
               self.xPos, " Y = ", self.yPos


# returns -1, 0, 1  with equal probability
def randomMove(jump):
    return random.randint(-1, 1)*jump
