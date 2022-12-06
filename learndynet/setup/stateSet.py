import xml.etree.ElementTree as ET
import copy
import numpy as np
from learnDyNet.learndynet.setup.config import Config

class StateSet:
    def __init__(self,config):
        self.__config=config
        self.__stateSet=[]
        self.__tree=ET.parse(self.__config.pathStates)
        self.__states_xml=self.__tree.getroot()
        self.__allowedActionSet={}
        # random seed init state mode
        self.__rdStateMode=    np.random.RandomState(self.__config.seedInitStateMode)

    def setModes(self,modes):           self.__modes=modes
    def setDirections(self,directions): self.__directions=directions



    def initStates(self):
        self.__stateSet=self.initStates_param(self.__config.modes,self.__config.directions,self.__config.maxNumberOfEdges)
        self.__config.numStates=len(self.__stateSet)
    def initStates_param(self,modes,directions,maxNumberOfLines):
        B=[[]]
        if maxNumberOfLines==0:
            return B
        elif maxNumberOfLines==1:
            print (modes,directions)
            for m in modes:
                for d in directions:
                    B.append([[m,d,self.__getCost(m)]]) #    print ([m,d,self.__getCost(m)])
            return B
        elif maxNumberOfLines==2:
            B=[[]]  #print (modes,directions)
            for m in modes:
                for d in directions:
                    B.append([[m,d,self.__getCost(m)]]) # print ([m,d,self.__getCost(m)])

            for m1 in modes:
                for m2 in modes:
                    for d1 in directions:
                        for d2 in directions:            B.append([[m1,d1,self.__getCost(m1)],[m2,d2,self.__getCost(m2)]])
            return B
        else: print ("maxNumberOfLines =",maxNumberOfLines, "is not implemented")

    def getStateSet(self):          return self.__stateSet
    def getAllowedActionSet(self):  return self.__allowedActionSet
    def getState(self,pos):         return self.__stateSet[pos]
    def getNstates(self):           return len(self.__stateSet)
    def getRandomState(self):       return self.getState(self.__rdStateMode.randint(0,len(self.__stateSet)))

    def getAllowedActions(self,state):
        return self.__allowedActionSet[self.getStatePos(state)]
    def getAllowedActionsPos(self,statePos):
        return self.__allowedActionSet[statePos]
    def getStatePos(self,state):
        try:                return self.__stateSet.index(state)
        except ValueError:
            print ("crisi --------------------------------------------",state)
            print (len(self.__stateSet),self.__stateSet)
            quit()
    def setAllowedActions(self, actions):
        allowedActionsSet={}
        for posState in range(len(self.__stateSet)):
            if len(self.__stateSet[posState])==0:   allowedActionsSet[posState]=self.__findPosVals(actions,"add")
            elif len(self.__stateSet[posState])==1:
                allowedActionsSet[posState]=self.__findPosVals(actions,"ed_1")+self.__findPosVals(actions,"add")
                if self.__stateSet[posState][0][0]=="walk" and self.__stateSet[posState][0][1]=="from-to": allowedActionsSet[posState]+=self.__findPosVals(actions,"rem_1_ed_walk_from-to")
                if self.__stateSet[posState][0][0]=="walk" and self.__stateSet[posState][0][1]=="to-from": allowedActionsSet[posState]+=self.__findPosVals(actions,"rem_1_ed_walk_to-from")
                if self.__stateSet[posState][0][0]=="bike" and self.__stateSet[posState][0][1]=="from-to": allowedActionsSet[posState]+=self.__findPosVals(actions,"rem_1_ed_bike_from-to")
                if self.__stateSet[posState][0][0]=="bike" and self.__stateSet[posState][0][1]=="to-from": allowedActionsSet[posState]+=self.__findPosVals(actions,"rem_1_ed_bike_to-from")
                if self.__stateSet[posState][0][0]=="car" and self.__stateSet[posState][0][1]=="from-to": allowedActionsSet[posState]+=self.__findPosVals(actions,"rem_1_ed_car_from-to")
                if self.__stateSet[posState][0][0]=="car" and self.__stateSet[posState][0][1]=="to-from": allowedActionsSet[posState]+=self.__findPosVals(actions,"rem_1_ed_car_to-from")
            elif len(self.__stateSet[posState])==2:
                allowedActionsSet[posState]=self.__findPosVals(actions,"mode")+self.__findPosVals(actions,"direction")
                if self.__stateSet[posState][0][0]=="walk" and self.__stateSet[posState][0][1]=="from-to": allowedActionsSet[posState]+=self.__findPosVals(actions,"rem_1_ed_walk_from-to")
                if self.__stateSet[posState][0][0]=="walk" and self.__stateSet[posState][0][1]=="to-from": allowedActionsSet[posState]+=self.__findPosVals(actions,"rem_1_ed_walk_to-from")
                if self.__stateSet[posState][0][0]=="bike" and self.__stateSet[posState][0][1]=="from-to": allowedActionsSet[posState]+=self.__findPosVals(actions,"rem_1_ed_bike_from-to")
                if self.__stateSet[posState][0][0]=="bike" and self.__stateSet[posState][0][1]=="to-from": allowedActionsSet[posState]+=self.__findPosVals(actions,"rem_1_ed_bike_to-from")
                if self.__stateSet[posState][0][0]=="car" and self.__stateSet[posState][0][1]=="from-to": allowedActionsSet[posState]+=self.__findPosVals(actions,"rem_1_ed_car_from-to")
                if self.__stateSet[posState][0][0]=="car" and self.__stateSet[posState][0][1]=="to-from": allowedActionsSet[posState]+=self.__findPosVals(actions,"rem_1_ed_car_to-from")
                if self.__stateSet[posState][1][0]=="walk" and self.__stateSet[posState][1][1]=="from-to": allowedActionsSet[posState]+=self.__findPosVals(actions,"rem_2_ed_walk_from-to")
                if self.__stateSet[posState][1][0]=="walk" and self.__stateSet[posState][1][1]=="to-from": allowedActionsSet[posState]+=self.__findPosVals(actions,"rem_2_ed_walk_to-from")
                if self.__stateSet[posState][1][0]=="bike" and self.__stateSet[posState][1][1]=="from-to": allowedActionsSet[posState]+=self.__findPosVals(actions,"rem_2_ed_bike_from-to")
                if self.__stateSet[posState][1][0]=="bike" and self.__stateSet[posState][1][1]=="to-from": allowedActionsSet[posState]+=self.__findPosVals(actions,"rem_2_ed_bike_to-from")
                if self.__stateSet[posState][1][0]=="car" and self.__stateSet[posState][1][1]=="from-to": allowedActionsSet[posState]+=self.__findPosVals(actions,"rem_2_ed_car_from-to")
                if self.__stateSet[posState][1][0]=="car" and self.__stateSet[posState][1][1]=="to-from": allowedActionsSet[posState]+=self.__findPosVals(actions,"rem_2_ed_car_to-from")
        self.__allowedActionSet=allowedActionsSet

    def getStateFromAction(self,state,action):
        newState=copy.deepcopy(state)
        if "ed_1_mode" in action:
            newMode=action.split("_")[3]
            newCost=self.__getCost(newMode)
            newState[0][0]=newMode
            newState[0][2]=newCost
        elif "ed_2_mode" in action:
            newMode=action.split("_")[3]
            newCost=self.__getCost(newMode)
            newState[1][0]=newMode
            newState[1][2]=newCost
        elif "direction" in action:
            newDirection=action.split("_")[3]
            if "ed_1_" in action:   newState[0][1]=newDirection
            else:                   newState[1][1]=newDirection
        elif "add" in action:
            newMode=action.split("_")[3]
            newDirection=action.split("_")[4]
            newCost=self.__getCost(newMode)
            newState.append([newMode,newDirection,newCost])
        elif "rem_1" in action:     newState.pop(0)
        else:
            newState.pop(1)
        return newState

    def __findVals(self,actions,val):
        l=[]
        for a in actions:
            if val in a: l.append(a)
        return l

    def __findPosVals(self,actions,val):
        l=[]
        for i in range(len(actions)):
            if val in actions[i]: l.append(i)
        return l

    def __getCost(self,mode):
        if mode=="walk":    return self.__config.cost_walk
        elif mode=="bike":   return self.__config.cost_bike
        else:               return self.__config.cost_car

class State:
    def __init__(self,idState,mode,direction,cost,nEdgePerDirection):
        self.__idState=idState
        self.__mode=mode
        self.__direction=direction
        self.__cost=cost
        self.__nEdgePerDirection=nEdgePerDirection
        self.__map={"idState":idState,"mode":mode,"direction":direction,"cost":cost,"nEdgePerDirection":nEdgePerDirection}

    def getMap(self):           return self.__map

def __test(run):
    if run:
        print ("test")
        pathConfig="/media/mtirico/DATA/project/learnDyNet/learnDyNet/scenarios/grid_01/config.xml"

        modes=["walk","bike","car"]
        directions=["from-to","to-from"]
        config=Config(pathConfig)
        sas=StateSet(config)
        sas.setModes(modes)
        sas.setDirections(directions)

__test(False)
