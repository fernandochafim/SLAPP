#ModelSwarm.py
import Tools
from Agent import *
from WorldState import *
from ActionGroup import *
import random
import os
from mActions import *
from turtle import *

task="0 0".split()

class ModelSwarm:
    def __init__(self, nAgents, worldXSize, worldYSize, project0):
        global task, project
        project=project0

        # the environment
        task="0 0".split() #in case of repeated execution without restarting the shell 
        self.ff="" #in case of repeated execution without restarting the shell
        self.nAgents = nAgents
        self.agentList = []
        self.worldStateList=[]

        self.worldXSize= worldXSize
        self.worldYSize= worldYSize

        # types of the agents
        agTypeFile=open("./"+project+"/agTypeFile.txt","r")
        self.types=agTypeFile.read().split()
        agTypeFile.close()
        #print self.types

        # operating sets of the agents
        try:
            agOperatingSetFile=open("./"+project+"/agOperatingSets.txt","r")
            self.operatingSets=agOperatingSetFile.read().split()
        except:
            print 'Warning: operating sets not found.'
            agOperatingSetFile = False
            self.operatingSets=[]
        if agOperatingSetFile: agOperatingSetFile.close()
        #print self.operatingSets


        dictExe={}
        dictExe["project"]=project
        execfile("./$$slapp$$/convert_xls_txt.py",dictExe)

    # objects
    def buildObjects(self):
        for i in range(1):
            aWorldState = WorldState(i)
            self.worldStateList.append(aWorldState)

        leftX =int(-self.worldXSize/2)
        rightX=int(self.worldXSize-1 -self.worldXSize/2) 
        bottomY =int(-self.worldYSize/2)
        topY=int(self.worldYSize-1 -self.worldYSize/2) 

        # internal agents
        for i in range(self.nAgents):
            anAgent = Agent(i, self.worldStateList[0],
                    random.randint(leftX,rightX), 
                    random.randint(bottomY,topY), leftX,rightX,
                    bottomY,topY,agType="bland")
            self.agentList.append(anAgent)
        print

        # external agents, RELATED TO THE SPECIFIC project
        files=os.listdir("./"+project)

        for agType in self.types:
            if not agType+".txt" in files: print "No", agType,\
               "agents: lacking the specific file", agType+".txt"

        for opSet in self.operatingSets:
            if not opSet+".txt" in files: print "No", opSet,\
               "agents: lacking the specific file", opSet+".txt"
        print

        for agType in self.types:
         if agType+".txt" in files:
           f=open("./"+project+"/"+agType+".txt","r")
           for line in f:
            if line.split() != []:
               num=int(line.split()[0])
               print "creating "+agType+": agent #", num
               #print line.split()

               # specialized creation function for each model
               # form mActions.py in the model folder

               createTheAgent(self,line,num,leftX,rightX,bottomY,topY,agType)
               #explictly pass self, here we use a function

           f.close()

        for opSet in self.operatingSets:
         if opSet+".txt" in files:
           f=open("./"+project+"/"+opSet+".txt","r")
           for line in f:
               if line.split() != []:
                num=int(line.split()[0])
                for anAgent in self.agentList:
                    if anAgent.number == num:
                        anAgent.setAnOperatingSet(opSet)
                        print "including agent #", num, \
                              "into the operating set", opSet
           f.close()     

        if self.operatingSets != []:
         for anAgent in self.agentList:
            anAgent.setContainers()

         for anAgent in self.agentList:
            anAgent.setAgentList(self.agentList)


        print
            

    # actions
    def buildActions(self): 

        modelActions=open("./"+project+"/modelActions.txt")
        mList=modelActions.read().split()
        modelActions.close()

        self.actionList = mList
        #print self.actionList

        # look at basic case schedule, where "move" represents an example of mandatory
        # action (in our case generating also a dynamic "jump" action) and
        # "read_script" represents an external source of actions
        # or, without reading the external schedule (anyway, in the case
        # above, if you do not put a schedule.txt or a schedule.xls file in
        # program folder, the "read_script" step simply has no effect)

        # basic actionGroup

        self.actionGroup0 = ActionGroup ()
        self.actionGroup0.do = do0 # do is a variable linking a method

        self.actionGroup1 = ActionGroup ()
        self.actionGroup1.do = do1 # do is a variable linking a method

        # to create other actionGroup ..,
        #self.actionGroup2 = ActionGroup (self.actionList[?])
        #self.actionGroup2.do = do2 # do is a variable linking a method
        # etc.

        # this actionGroup is the schedule, which is generalized
        # so it is not moved in the actions.py specific to the project
        # the task number is huge (100), considering it to be the last one
        # the name is identified as the last one, with -1
        self.actionGroup100 = ActionGroup ("read_script") # the last
        def do100(address, cycle):
            global task

            actionDictionary[self.actionGroup100.getName()]=self.actionGroup100

            while True:
                if task[0]=="#":
                    if int(task[1]) > cycle: break

                task=read_s(self.ff)
                #print "***", task

                if task[0]=="#":
                    if int(task[1]) > cycle: break
                if task[0]=="0": break

                #if task[0] is all or an agent type
                if check(task[0],self.types):
                    # keep safe the original list
                    localList=[]
                    for ag in address.agentList:
                        if   task[0]=="all": localList.append(ag)
                        elif task[0]==ag.getAgentType(): localList.append(ag)
                    # never in the same order (please comment if you want to keep
                    # always the same sequence
                    random.shuffle(localList)
                    # apply method only to a part of the list, or, which is the
                    # same, with the given probability to each element of the list
                    self.share=0
                    try:    self.share = float(task[1]) # does task[1] contains
                                                        # a int or float number?
                    except: pass
                    
                    if self.share > 0:
                        tmpList=localList[:]
                        del localList[:]
                        for i in range(len(tmpList)):
                            if random.random() <= self.share:
                                localList.append(tmpList[i])

                    if self.share < 0: # in case, an abs. number of agent *(-1)
                        tmpList=localList[:]
                        del localList[:]
                        for i in range(int(-self.share)):
                            random.shuffle(tmpList)
                            if tmpList != []:
                                localList.append(tmpList.pop(0))

                    # apply
                    if len(localList)>0:
                        self.applyFromSchedule(localList,task)

                #if task[0] is an opSet
                if task[0] in address.operatingSets:
                    # keep safe the original list
                    localList=[]
                    for ag in address.agentList:
                        if task[0] in ag.getOperatingSetList():
                            localList.append(ag)
                    if localList==[]:
                        print "Warning, no agents in operating set", task[0]
                    # never in the same order (please comment if you want to keep
                    # always the same sequence
                    random.shuffle(localList)
                    # apply method only to a share of the list
                    self.share=0
                    try:    self.share = float(task[1])   # does task[1] contains
                                                          # an int or float number?
                    except: pass

                    
                    if self.share > 0:
                        tmpList=localList[:]
                        del localList[:]
                        for i in range(len(tmpList)):
                            if random.random() <= self.share:
                                localList.append(tmpList[i])

                    if self.share < 0: # in case, an abs. number of agent *(-1)
                        tmpList=localList[:]
                        #print "*********************", tmpList
                        del localList[:]
                        for i in range(int(-self.share)):
                            random.shuffle(tmpList)
                            if tmpList != []:
                                localList.append(tmpList.pop(0))
                        #print "*********************", localList

                    # apply
                    if len(localList)>0:
                        self.applyFromSchedule(localList,task)

                if task[0]=='WorldState':
                    self.share=0
                    localList=address.worldStateList[:]
                    self.applyFromSchedule(localList,task)
                   
        self.actionGroup100.do = do100 # do is a variable linking a method
    
    



    # run a step
    def step(self,cycle):
            global task

            step=self.actionList[:]

            while len(step)>0:
                subStep=extractASubStep(step)
                #print "*****************", subStep
                found=False

                if subStep == "reset":
                        found=True
                        self.actionGroup0.do(self)
                if subStep == "move":
                        found=True
                        self.actionGroup1.do(self)
                    # self here is the model env.
                    # not added automatically
                    # being do a variable
                    

                # external schedule, in pos. -1
                if subStep == "read_script":
                        found=True
                        if self.ff=="":
                            try: self.ff=open("./"+project+"/schedule.txt","r")
                            except: pass
                        self.actionGroup100.do(self,cycle)
                    # self here is the model env.
                    # not added automatically
                    # being do a variable

                # other steps
                if not found:
                 found=otherSubSteps(subStep, self)    

                if not found: print "Warning: step %s not found in Model" % subStep



    # from external schedule (script)
    def applyFromSchedule(self,localList,task):


        if task[0]=='WorldState':
            if task[2]=='setGeneralMovingProb':
                prob = 1
                try:  prob = float(task[1]) # does task[1] contains
                                            # a number?
                except: pass
            d={}
            d['generalMovingProb']=prob
            try: exec "askEachAgentInCollection(localList,"+task[0]+"."+task[2]+", **d)"
            except: pass


        #if task[0] is 'all' or a type of agent
        if check(task[0],self.types):
            if self.share!=0:
                try: exec "askEachAgentInCollection(localList,Agent"+"."+task[2]+")"
                except:
                    print "Warning, method", task[2],"does not exist in agents"
                    pass
            else:
                try: exec "askEachAgentInCollection(localList,Agent"+"."+task[1]+")"
                except:
                    print "Warning, method", task[1],"does not exist in agents"
                    pass

        #if task[0] is an opSet
        if task[0] in self.operatingSets:
            if self.share!=0:
                try: exec "askEachAgentInCollection(localList,Agent"+"."+task[2]+")"
                except:
                    print "Warning, method", task[2],"does not exist in agents"
                    pass
            else:
                try: exec "askEachAgentInCollection(localList,Agent"+"."+task[1]+")"
                except:
                    print "Warning, method", task[1],"does not exist in agents"
                    pass



    # agent list
    def getAgentList(self):
        return self.agentList

    # file address
    def getFile(self):
        return self.ff

# tools, read_s
def read_s(f):
    if f != "":
        try:
            task=f.readline()
            if task=='':task='0 0'
        except:
            task='0 0'
    else: task='0 0'

    return task.split()

# check if it is an agent
def check(s,aList):
    found=False
    if s.find("all")==0  : found=True
    if s.find("bland")==0: found=True
    for name in aList:
        if s.find(name)==0:found=True
    return found
