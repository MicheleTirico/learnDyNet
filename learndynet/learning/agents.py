import copy

import networkx as nx
import numpy as np

class Agents:
    def __init__(self,config,network,stateSet):
        self.__config=config
        self.__network=network
        self.__stateSet=stateSet
        self.__agents={}
        self.__G= self.__network.getGraph()

    def setMobility(self,mobility):     self.__mobility=mobility
    def setIndividuals(self,individuals):     self.__individuals=individuals

    def initAgents(self):        self.__initAgents_mode(self.__config.initStateMode)

    def __initAgents_mode(self,mode):
        # attrib agents
        attr_id=nx.get_edge_attributes(self.__G,"id")
        attr_length=nx.get_edge_attributes(self.__G,"length")
        for e in attr_id.keys():        #
            # get state
            state=None
            if mode=="same":            state=self.__stateSet.getState(self.__config.initState)
            elif mode=="random":        state=self.__stateSet.getRandomState()
            agent=Agent(attr_id[e],self.__config,self.__network,self.__stateSet)
            agent.setLength(attr_length[e])
            agent.setVertices(e[0],e[1])
            agent.appendState(state)
        #    agent.initQtab(self.__config.numStep,self.__config.numStates,self.__config.numActions)
         #   agent.initQtabMap(self.__config.numStep,self.__config.numStates,self.__config.numActions)
            agent.initQtabList(self.__config.numStates,self.__config.numActions)
            self.__agents[attr_id[e]]=agent

    def getAgents(self):        return self.__agents
    def getAgent(self,id):      return self.__agents[id]
    def getAgentVertices(self,v0,v1):
        for id in self.__agents:
            a=self.__agents[id]
            vertices=a.getVertices()
            if (v0==vertices[0] and v1==vertices[1]) or (v0==vertices[1] and v1==vertices[0]):                return a

    def updateReward(self,step):
        for id , agent in self.__agents.items():
            num_ind=agent.get_num_ind_pos(step)
            sum_utility=agent.get_sum_utility_pos(step)
            #   print (self.__mobility.getNumberTripNotFunded()[step-1],len(self.__individuals.getIndividuals()))
            penalty=self.__mobility.getNumberTripNotFunded()[step-1]/(3*len(self.__individuals.getIndividuals()))
            #if sum_utility==0:   sum_utility=self.__config.rewardNoTripFunded
            try:
                agent.append_reward(round(penalty*sum_utility/num_ind,3))
           #     print ("reward",penalty,round(sum_utility/num_ind,3))
            except ZeroDivisionError:   agent.append_reward(sum_utility)

class Agent(Agents):
    def __init__(self,id,config,network,stateSet):
        super().__init__(config, network,stateSet)
        self.__config=config
        self.__network=network
        self.__stateSet=stateSet
        self.__id=id
        self.__vertices=()
        self.__length=0
        self.__states=[]
        self.__statesPos=[]
        self.__reward=[]
        self.__num_ind=[0]
        self.__sum_utility=[0]
        self.__actions=[]
        self.__numStep=self.__config.numStep
        self.__stateTested=[]
        self.__qtabMap={}
        self.__qtabList=[[[]]]

    def getId(self):            return id
    def getListStateNotTested(self):
        for state in self.__states:
            statePos=self.__stateSet.getStatePos(state)
            self.__statesPos.append(statePos)
        self.__stateTested=[*set(self.__statesPos)]
        return self.__stateTested
# list
    def initQtabList(self,numStates,numActions):
        self.__qtabList[0]=[[0 for _ in range(numActions)] for _ in range(numStates)]

    def getQtabList(self):       return self.__qtabList

    def setQtabList(self,step,statePos,actionPos,qval):
        tab=copy.deepcopy(self.__qtabList[step-1])
        tab[statePos][actionPos]=round(qval,3)
        self.__qtabList.append(tab)

    # display
    # ---------------------------------------------------------------------------------------
    def displayQtable(self):    print (self.__qtab)
    def displayQtableStep(self):
        for step in range(len(self.__qtab)):    print ("step:",step,"\n",self.__qtab[step])

    def getActions(self):           return self.__actions
    def getActionPos(self,pos):     return self.__actions[pos]
    def appendAction(self,action): self.__actions.append(action)


    def getVertices(self):          return self.__vertices
    def setVertices(self,v0,v1):   self.__vertices=(v0,v1)

    def setLength(self,length):   self.__length=length
    def getLength(self):            return self.__length

    def appendState(self,state):   self.__states.append(state)
    def getStates(self):           return self.__states
    def getState(self,step):        return self.__states[step]

    def set_num_ind(self,pos,num_ind):
        if len(self.__num_ind)==0: self.append_num_ind(num_ind)
        else:        self.__num_ind[pos]=num_ind
    def append_num_ind(self,num_ind):        self.__num_ind.append(num_ind)

    def set_sum_utility(self,pos,sum_utility):
        if len(self.__sum_utility)==0: self.append_sum_utility(sum_utility)
        else:        self.__sum_utility[pos]=sum_utility
    def append_sum_utility(self,sum_utility):        self.__sum_utility.append(sum_utility)

    def set_reward(self,pos,reward):
        if len(self.__reward)==0: self.append_reward(reward)
        else:        self.__reward[pos]=reward
    def append_reward(self,reward):        self.__reward.append(reward)

    def get_sum_utility(self):        return self.__sum_utility
    def get_num_ind(self):        return self.__num_ind
    def get_reward(self):        return self.__reward

    def get_num_ind_pos(self,pos):
        try: return self.__num_ind[pos]
        except IndexError:
            self.__num_ind.append(0)
            return self.__num_ind[pos]
    def get_sum_utility_pos(self,pos):
        try: return self.__sum_utility[pos]
        except IndexError:
            self.__sum_utility.append(0)
            return self.__sum_utility[pos]
    def get_reward_pos(self,pos):
        try: return self.__reward[pos]
        except IndexError:
            self.__reward.append(0)
            return self.__reward[pos]

